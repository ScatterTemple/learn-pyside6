from PySide6.QtGui import QStandardItemModel, QStandardItem


def set_treeview(treeview, table_models):
    model: QStandardItemModel = QStandardItemModel()

    root: QStandardItem = model.invisibleRootItem()

    for i, table_model in enumerate(table_models):
        root.setColumnCount(max(root.columnCount(), table_model.columnCount()))

        # table = QStandardItem(f'項目{i}テーブル')
        # table.appendColumn([QStandardItem(table_model.index(row, column).data()) for row in range(table_model.rowCount()) for column in range(table_model.columnCount())])
        # # table.appendColumn([table_model.item(row, column) for row in range(table_model.rowCount()) for column in range(table_model.columnCount())])
        # root.appendRow(table)


        table = QStandardItem(table_model.rowCount(), table_model.columnCount())
        table.setText(f'項目{i}テーブル')
        # table = QStandardItem(f'項目{i}テーブル')
        # table.setRowCount(table_model.rowCount())
        # table.setColumnCount(table_model.columnCount())
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table_model.item(row, col)
                table.setChild(row, col, QStandardItem(item))

        root.appendRow(table)


    treeview.setModel(model)
