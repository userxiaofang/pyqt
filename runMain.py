import sys
import test
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindows = QMainWindow()
    ui = test.Ui_MainWindow()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())



