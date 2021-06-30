from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.ui.btnHello.clicked.connect(self.HelloWorld)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def HelloWorld(self):
        print("Hello World !!!")
        QMessageBox.about(self, "HelloWorld", "Hello World !!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, False)
    w = MainWindow()
    #   Disable maximize window button
    w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    w.show()
    sys.exit(app.exec_())
