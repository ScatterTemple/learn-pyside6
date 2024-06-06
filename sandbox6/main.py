import sys

from PySide6.QtWidgets import (QApplication, QWizard)

from ui_wizard import Ui_Wizard
from table_model import PrmTableModel, ObjTableModel, ComboBoxDelegate


import _p


# noinspection PyMethodMayBeStatic
class MainWizard(QWizard):

    def set_ui(self, ui):
        self._ui = ui

    def load_prm(self):
        ...

    def load_obj(self):
        ...

    def load_model(self):
        prj = _p._dummy.prj
        model = _p._dummy.model
        self._ui.plainTextEdit_prj.setText(prj)
        self._ui.plainTextEdit_model.setText(model)

    def connect_process(self):
        print(f'Connected! (pid: {_p._dummy.pid})')  # TODO: show dialog


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wizard = MainWizard()

    prm_table_model = PrmTableModel()  # モデルの作成
    obj_table_model = ObjTableModel()  # モデルの作成

    ui_wizard = Ui_Wizard()
    ui_wizard.setupUi(wizard)
    ui_wizard.tableView_prm.setModel(prm_table_model)  # モデルをビューに設定
    ui_wizard.tableView_obj.setModel(obj_table_model)  # モデルをビューに設定

    delegate = ComboBoxDelegate(obj_table_model)  # デリゲートの作成
    ui_wizard.tableView_obj.setItemDelegate(delegate)  # デリゲートをビューに設定

    from tree_model import set_treeview
    set_treeview(ui_wizard.treeView, [prm_table_model, obj_table_model])

    wizard.show()  # ビューの表示
    sys.exit(app.exec())  # アプリケーションの実行
