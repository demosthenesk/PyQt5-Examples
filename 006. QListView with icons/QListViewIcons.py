import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setFont(QtGui.QFont("Helvetica", 8, QtGui.QFont.Normal, italic=False))
        lay = QtWidgets.QVBoxLayout(self)

        self.listView = QtWidgets.QListView()
        lay.addWidget(self.listView)

        self.entry = QtGui.QStandardItemModel()
        self.listView.setModel(self.entry) 
        self.listView.setSpacing(5)

        for i, text in enumerate(["USA", "RUSSIA", "UK"]):
            it = QtGui.QStandardItem(text)
            self.entry.appendRow(it)

            it.setData(QtGui.QIcon(os.path.join('images', 'flag{}.png'.format(i))),
                                   QtCore.Qt.DecorationRole)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
