from copy import copy

from .block import Block


class Loop(Block):
    def apply(self, items):
        original = self.project()
        items = list(items)

        if not items:
            return

        first_item = items[0]
        block = self

        block.apply_template(first_item)

        for c in copy(block._children):
            c.apply(first_item[c.name])
        # if "placements" in first_item:
        #     # print(block.name, block._children)
        #     block._children[0].apply(first_item["placements"])

        for item in items[1:]:

            shift = block.max_row + 1 - original.min_row
            block = original.project(shift_rows=shift)

            # print(self._parent, self._parent._children_map["ads"])
            self._parent.insert(block)

            block.apply_template(item)
            for c in copy(block._children):
                c.apply(item[c.name])
            # if "placements" in item:
            #     block._children[0].apply(item["placements"])
