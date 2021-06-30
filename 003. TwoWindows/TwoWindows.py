from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import *
from frmWindowTwo import *
import sys

class frmWindowTwo(QWidget):
    def __init__(self, parent=None):
        super(frmWindowTwo, self).__init__(parent)
        self.ui = Ui_frmWindowTwo()
        self.ui.setupUi(self)
        self.center()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.ui.btnHello.clicked.connect(self.frmWindowTwoShow)
        # frmWindowTwo form
        self.frmWindowTwo = frmWindowTwo()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def frmWindowTwoShow(self):
        self.frmWindowTwo.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, False)
    w = MainWindow()
    #   Disable maximize window button
    w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    w.show()
    sys.exit(app.exec_())
