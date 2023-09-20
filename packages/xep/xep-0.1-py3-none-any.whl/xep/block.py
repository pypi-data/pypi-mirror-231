from xep.geometry import GeometryBlock


class Block(GeometryBlock):
    def __init__(self, *args, name=None, template=None, **kwargs):
        self._template = template
        self.name = name
        self._children_map = dict()
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.name}({self._range})"

    def add_child(self, child):
        super().add_child(child)
        self._children_map[child.name] = child

    def project(self, *args, **kwargs):
        new_block = super().project(*args, **kwargs)
        new_block._template = self._template
        new_block.name = self.name
        return new_block

    def apply_template(self, context):
        if self._template:
            self._template.apply(
                self._worksheet,
                self._range,
                context,
                apply_row_styles=True
            )

    def apply(self, context):
        self.apply_template(context)
