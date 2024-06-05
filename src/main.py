# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QCheckBox, QGridLayout, QLabel, QLineEdit,
                               QMessageBox, QRadioButton, QVBoxLayout, QWizard,
                               QWizardPage)

from wiz.ui_wizard import Ui_Wizard

from my_table_model import MyTableModel


if __name__ == "__main__":
    app = QApplication(sys.argv)

    wizard = Ui_Wizard()

    empty = QWizard()
    wizard.setupUi(empty)

    table_view = wizard.tableView

    model = MyTableModel()
    table_view.setModel(model)

    empty.show()
    sys.exit(app.exec())
