import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from LamLai import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.stackedWidget.setCurrentWidget(self.uic.Home)

        self.uic.Screen1_Button.clicked.connect(self.showScreen_1)
        self.uic.Screen2_Button.clicked.connect(self.showScreen_2)
        self.uic.Screen3_Button.clicked.connect(self.showScreen_3)
        self.uic.Home_Button.clicked.connect(self.showHome)

    def show(self):
        self.main_win.show()
    def showScreen_1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Screen1)
    def showScreen_2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Screen2)
    def showScreen_3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Screen3)
    def showHome(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.Home)

if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())