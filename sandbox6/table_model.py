from typing import Optional

import PySide6

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QStandardItemModel, QStandardItem)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QTableView, QTextEdit,
    QWidget, QWizard, QWizardPage, QStyledItemDelegate)
import sys
from PySide6.QtWidgets import (
    QApplication, QTableView, QItemDelegate, QComboBox, QSpinBox
)
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, QObject


import _p


def _isnumeric(exp):
    try:
        float(str(exp))
        isnumeric = True
    except ValueError:
        isnumeric = False
    return isnumeric


class PrmTableModel(QStandardItemModel):
    """A table for determining whether to use Femtet variables in optimization.

    use      | name | expression   | lb             | ub             | test
    --------------------------------------------------------------------------
    checkbox | str  | float or str | float or empty | float or empty | float

    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_data()

    def load_data(self):
        self.setHorizontalHeaderLabels(['use', 'name', 'expression', 'lb', 'ub', 'test'])
        # load prm
        names = _p._dummy.get_prm_names()
        expressions = _p._dummy.get_prm_expressions()

        for row, (name, exp) in enumerate(zip(names, expressions)):
            self.insertRow(self.rowCount())
            exp = str(exp)
            use = _isnumeric(exp)
            row_data = [use, name, exp, '0.0', '1.0', exp]  # TODO: implement delegate
            for col, value in enumerate(row_data):
                self.setItem(row, col, QStandardItem(value))

        tl = self.createIndex(0, 0)
        br = self.createIndex(5, len(names)-1)
        self.dataChanged.emit(tl, br)


class ObjTableModel(QStandardItemModel):
    """A table for determining whether to use Femtet variables in optimization.

    use      | name | direction   | value
    ----------------------------------------------
    checkbox | str  | combobox    | float or empty

    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_data()

    def load_data(self):
        self.setHorizontalHeaderLabels(['use', 'name', 'direction', 'value'])

        # load obj
        names = _p._dummy.get_output_names()
        for row, name in enumerate(names):
            self.insertRow(self.rowCount())
            row_data = [True, name, 'Maximize', None]  # TODO: implement delegate
            for col, value in enumerate(row_data):
                if col == 0:
                    item = QStandardItem(value)
                    item.setCheckable(True)
                    self.setItem(row, col, item)
                else:
                    self.setItem(row, col, QStandardItem(value))

        tl = self.createIndex(0, 0)
        br = self.createIndex(5, len(names)-1)
        self.dataChanged.emit(tl, br)


class ComboBoxDelegate(QStyledItemDelegate):

    def __init__(self, model):
        super().__init__()
        self._model = model

    def createEditor(self, parent, option, index):
        col, row = index.column(), index.row()
        col_name = self._model.horizontalHeaderItem(col).text()
        print(col_name)
        if col_name == 'direction':
            # コンボボックスエディタを作成
            comboBox = QComboBox(parent)
            comboBox.addItems(['Maximize', 'Minimize', 'Specify'])
            return comboBox
        elif col_name == 'use':
            return
        # elif col_name == 'value':
        #     # スピンボックスエディタを作成
        #     spinBox = QSpinBox(parent)
        #     spinBox.setRange(0, 100)
        #     return spinBox
        return super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        col, row = index.column(), index.row()
        col_name = self._model.horizontalHeaderItem(col).text()
        if col_name == 'direction':
            # コンボボックスにデータを設定
            value = index.model().data(index, Qt.EditRole)
            editor.setCurrentText(value)
        # elif col_name == 'value':
        #     # スピンボックスにデータを設定
        #     value = index.model().data(index, Qt.EditRole)
        #     editor.setValue(float(value))
        else:
            super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        col, row = index.column(), index.row()
        col_name = self._model.horizontalHeaderItem(col).text()
        if col_name == 'direction':
            # コンボボックスのデータをモデルに設定
            model.setData(index, editor.currentText(), Qt.EditRole)
        # elif col_name == 'value':
        #     # スピンボックスのデータをモデルに設定
        #     model.setData(index, editor.value(), Qt.EditRole)
        else:
            super().setModelData(editor, model, index)


# これを使いたければ QtDesigner にカスタムとして登録したほうがよい
class SingleClickTableView(QTableView):
    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid() and index.column() == 1:
            self.edit(index)
        super(SingleClickTableView, self).mousePressEvent(event)

