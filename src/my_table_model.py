import sys
import logging
logger = logging.getLogger('learn_QTable')
logger.setLevel(logging.INFO)  # https://forum.qt.io/topic/129370/pyside6-disables-logging-debug-level/5

from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QMessageBox, QCheckBox

from dummy_process import DummyProcess


_process_obj = DummyProcess()


# noinspection PyUnresolvedReferences
class CustomTableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._data = [[]]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def data(self, index, role=Qt.DisplayRole):
        # getter
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self._data[index.row()][index.column()]
        return None

    def setData(self, index, value, role=Qt.EditRole):
        # setter
        row, col = index.row(), index.column()
        if role == Qt.EditRole:
            self._data[row][col] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])
            return True
        return False


# noinspection PyMethodOverriding,PyTypeChecker,PyArgumentList
class MyTableModel(CustomTableModel):
    """A table for determining whether to use Femtet variables in optimization.

    use       | name | expression   | lb             | ub             | test
    --------------------------------------------------------------------------
    QCheckBox | str  | float or str | float or empty | float or empty | float

    """

    def __init__(self):
        super().__init__()
        self._init_data()
        self.columns = ['use', 'name', 'expression', 'lb', 'ub', 'test']

    def _get_column(self, c: int):
        return self.columns[c]

    def flags(self, index):
        col_name = self._get_column(index.column())

        # name is uneditable
        if col_name == 'name':
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable

        # use is checkable
        elif col_name == 'use':
            return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsUserCheckable

        else:
            return super().flags(index)

    def setData(self, index, value, role=Qt.EditRole):
        # setter
        row, col = index.row(), index.column()
        col_name = self._get_column(col)

        # checkbox
        if role == Qt.CheckStateRole:
            checkbox: QCheckBox = self._data[row][col]
            current_state = checkbox.isChecked()
            checkbox.setChecked(not current_state)
            return True

        # the others
        elif role == Qt.EditRole:
            # float input rule
            if (col_name == 'lb') or (col_name == 'ub') or (col_name == 'test'):
                try:
                    float(value)  # 数値に変換できるかチェック
                except ValueError:
                    QMessageBox.warning(None, "Invalid Input", "The value must be a number.")
                    return False

            # expression input rule
            if col_name == 'expression':
                ...

            return super().setData(index, value, role)

        return False

    def _init_data(self):
        prm_names = _process_obj.GetVariableNames()
        tmp = []
        for prm_name in prm_names:
            expression = _process_obj.GetVariableExpression(prm_name)
            test = _process_obj.GetVariableValue(prm_name)
            lb = 0
            ub = 1
            tmp.append([QCheckBox(""), prm_name, expression, lb, ub, test])
        self._data = tmp
        index = self.createIndex(0, 0)
        self.dataChanged.emit(index, index, [Qt.DisplayRole, Qt.EditRole])

    def data(self, index, role=Qt.DisplayRole):
        row, col = index.row(), index.column()

        # checkbox
        col_name = self._get_column(col)
        if (col_name == 'use') and (role == Qt.CheckStateRole):
            checkbox: QCheckBox = self._data[row][col]
            return checkbox.isChecked()

        # the others
        else:
            return super().data(index, role)

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.columns[col]
        return None
