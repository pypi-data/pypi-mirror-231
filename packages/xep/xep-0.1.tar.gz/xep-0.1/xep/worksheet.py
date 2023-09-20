from openpyxl.worksheet.cell_range import CellRange
from xep.template.range import RangeTemplate
import yaml
import itertools
import copy
from xep.template.format import python_formatter

from .block import Block
from .loop import Loop
from .table import Table


class WorksheetTemplate:
    def __init__(self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet
        self.annotations = list()
        self._named_ranges = dict()

        self.title_template = self.worksheet.title
        self.multiply = False

        self.name = None
        self.context = None

        self._template = RangeTemplate(
            self.worksheet,
            CellRange(self.worksheet.dimensions),
            # excludes=[b._range for b in ws_blocks.values()]
        )

        self._load_annotations(cleanup=True)

        for a in self.annotations:
            if "sheet" in a:
                self.context = self.name = a["sheet"]["name"]
                self.multiply = a["sheet"].get("multiply", False)

        self.blocks_info = list(self._blocks_info())

    def _parse_annotation(self, text):
        if text.split(
                "\n", 1
        )[0].strip(
            "# \t"
        ).startswith(
            "template-annotation"
        ):

            return yaml.load(text, Loader=yaml.SafeLoader)
        else:
            return None

    def _load_annotations(self, cleanup=False):
        for cell in itertools.chain.from_iterable(self.worksheet.rows):
            if cell.comment:
                annotation = self._parse_annotation(
                    cell.comment.text
                )
                if annotation:
                    self.annotations.append(annotation)

                if cleanup:
                    cell.comment = None

    def _load_named_range(self, range_name, cleanup=False):

        # print(self.worksheet.defined_names)
        # TODO: workbook access
        # named_range = self.workbook.defined_names.get(
        #     range_name, self.workbook.index(self.worksheet)
        # )

        named_range = self.worksheet.defined_names.get(range_name)

        if named_range:
            destinations = list(named_range.destinations)
            assert len(destinations) == 1
            sheet_name, range_string = destinations[0]
            self._named_ranges[range_name] = CellRange(range_string)

            if cleanup:
                self.workbook.defined_names.delete(
                    range_name, self.workbook.index(self.worksheet)
                )
        else:
            raise KeyError(
                f"Can not find range with name \"{range_name}\" at page \"{self.worksheet.title}\""
            )

    def block_info(self, description):

        class ObjectAnnotation:
            def __init__(self, description):
                self.name = description["name"]
                self.type = description["type"]
                self.parent = description.get("parent", None)
                self.range = description.get("range", self.name)
                self.context = description.get("context", self.name)

            def __str__(self):
                return f"{self.name=}, {self.type=}, {self.range=}"

        ann = ObjectAnnotation(description)
        self._load_named_range(ann.range)
        return ann

    def _blocks_info(self):
        for a in self.annotations:
            if "name" in a:
                yield self.block_info(a)

    def apply(self, worksheet, context):

        worksheet.title = python_formatter(self.title_template, context)
        sheet_block = Block(
            worksheet,
            CellRange(worksheet.dimensions),
            name="root",
            template=RangeTemplate(
                worksheet,
                CellRange(worksheet.dimensions),
            )
        )

        all_blocks = dict()

        for block_annotation in self.blocks_info:

            block_range = copy.copy(self._named_ranges[block_annotation.range])
            # print(
            #     f"{self.worksheet.title}: {block_annotation}"
            # )

            if block_annotation.parent:
                parent = all_blocks[block_annotation.parent]
            else:
                parent = sheet_block

            if block_annotation.type == "block":
                BlockClass = Block
            elif block_annotation.type == "table":
                BlockClass = Table
            elif block_annotation.type == "loop":
                BlockClass = Loop
            else:
                raise ValueError()

            new_block = BlockClass(
                worksheet,
                block_range,
                name=block_annotation.name,
                template=RangeTemplate(
                    worksheet,
                    block_range,
                    # excludes=[b._range for b in block._children.values()]
                ),
                parent=parent
            )
            all_blocks[block_annotation.name] = new_block

        sheet_block.apply(context)

        for child in copy.copy(sheet_block._children):
            # TODO: error if not context for child
            child_context = context[child.name]
            child.apply(child_context)
