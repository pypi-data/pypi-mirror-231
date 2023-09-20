from .block import Block


class Table(Block):
    def apply(self, items):
        original = self.project()
        items = list(items)

        if not items:
            return

        first_item = items[0]
        block = self

        block.apply_template(first_item)

        item_size = 1

        if len(items) > 1:
            table_rows = block.project(shift_rows=item_size)

            if len(items) > 2:
                table_rows.expand(
                    (len(items) - 2) * item_size
                )

            self._parent.insert(table_rows)

            for index, item in enumerate(items[1:], 1):
                shift = index * item_size
                block = original.project(shift_rows=shift)
                table_rows.add_child(block)
                block.apply_template(item)
