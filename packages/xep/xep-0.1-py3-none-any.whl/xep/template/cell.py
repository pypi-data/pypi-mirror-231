import copy
import re

from openpyxl.cell import MergedCell
from openpyxl.formula.translate import Translator

from .format import python_formatter


class CellTemplate:
    RE_VARIABLE = re.compile(r"^{(?P<var_name>[\w.]+)}$")

    def __init__(self, origin_cell):
        self._origin_value = origin_cell.value
        self._merged = isinstance(origin_cell, MergedCell)
        self._translator = None
        self._var_name = None

        if isinstance(self._origin_value, str):
            match = self.RE_VARIABLE.match(self._origin_value)
            if match:
                self._var_name = match.group("var_name")
                self._apply_value = self._apply_variable_value
            elif self._origin_value.startswith("="):
                self._translator = Translator(
                    self._origin_value,
                    origin=origin_cell.coordinate
                )
                self._apply_value = self._apply_formula_value
            else:
                self._apply_value = self._apply_template_value
        else:
            self._apply_value = self._apply_static_value

        self._style = copy.copy(origin_cell._style)

    def _apply_value(self, cell, context: dict):
        return None

    def _apply_static_value(self, cell, context: dict):
        cell.value = self._origin_value

    def _apply_formula_value(self, cell, context: dict):
        cell.value = self._translator.translate_formula(
            dest=cell.coordinate
        )

    def _apply_variable_value(self, cell, context: dict):
        cell.value = context.get(self._var_name, cell.value)

    def _apply_template_value(self, cell, context: dict):
        try:
            cell.value = python_formatter(
                self._origin_value,
                context
            )
        except KeyError:
            cell.value = self._origin_value

    def apply(self, cell, context: dict):
        if isinstance(cell, MergedCell):
            return

        self._apply_value(cell, context)
        cell._style = self._style


class FakeCell(CellTemplate):
    def apply(self, cell, context: dict):
        pass
