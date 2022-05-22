from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
import pickle
import os


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("Jassa.ui", self)
        self.show()
        self.setFixedSize(281, 395)
        self.setWindowTitle("Jassa")
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

        self.plusbutton.clicked.connect(self.add_todo)
        self.minbutton.clicked.connect(self.remove_todo)
        self.actionLoad.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def add_todo(self):
        todo, confirmed = QInputDialog.getText(
            self, "Add Todo", "New todo:", QLineEdit.Normal)

        if confirmed and not todo.isspace():
            item = QStandardItem(todo)
            self.model.appendRow(item)
            file = "jassa.wav"
            os.system(file)

    def remove_todo(self):
        if len(self.listView.selectedIndexes()) != 0:
            selected = self.listView.selectedIndexes()[0]

            dailog = QMessageBox()
            dailog.setText(f"'{selected.data()}'Remove Kr Dia Jaye?")
            dailog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
            dailog.addButton(QPushButton("No"), QMessageBox.NoRole)

            if dailog.exec_() == 0:
                self.model.removeRow(selected.row())
            print('\a')

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "rb") as f:
                item_list = pickle.load(f)
                # pickle.load(item_list, f)
                self.model = QStandardItemModel()
                self.listView.setModel(self.model)
                for item in item_list:
                    self.model.appendRow(QStandardItem(item))

    def save_file(self):
        item_list = []
        for i in range(self.model.rowCount()):
            item_list.append(self.model.item(i).text())
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Todo Files (*.todo)", options=options)
        if filename != "":
            with open(filename, "wb") as f:
                pickle.dump(item_list, f)


app = QApplication([])
window = MyGUI()
app.exec_()
