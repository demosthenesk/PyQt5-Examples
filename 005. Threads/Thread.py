from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import *
import sys
import time


class RunThread(QtCore.QThread):
    counter_value = QtCore.pyqtSignal(int)  # define new Signal

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        self.is_running = True
        while self.counter < 100 and self.is_running is True:
            time.sleep(0.5)
            self.counter += 1
            self.counter_value.emit(self.counter)  # emit new Signal with value

    def stop(self):
        try:
            self.is_running = False
            self.terminate()
        except:
            pass

    def wait(self):
        try:
            self.is_running = False
            self.wait()
        except:
            pass

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.center()
        #Init progressBar
        self.ui.progressBar.setValue(0)
        #Buttons
        self.ui.btnRun.clicked.connect(self.StartThread)
        self.ui.btnStop.clicked.connect(self.WaitThread)
        self.ui.dial.sliderMoved.connect(self.SetLCD)
        #Init Thread
        self.MyThread = RunThread(parent=None, counter_start=0)

    def SetLCD(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    def WaitThread(self):
        self.MyThread.wait()

    def StartThread(self):
        self.MyThread.start()
        self.MyThread.counter_value.connect(self.SetProgressBarValue)

    def SetProgressBarValue(self):
        self.ui.progressBar.setValue(self.MyThread.counter)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, False)
    w = MainWindow()
    #   Disable maximize window button
    w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
    w.show()
    sys.exit(app.exec_())
