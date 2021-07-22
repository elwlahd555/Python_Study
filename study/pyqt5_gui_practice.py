import sys

from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, \
    QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()


    def initUI(self):




        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)


        self.setWindowTitle('My First Application')



        self.move(300, 300)
        self.resize(400, 200)
        self.setWindowIcon(QIcon('image.jpg'))
        self.setGeometry(300, 300, 300, 200)
        # btn = QPushButton('Quit', self)
        # btn.move(50, 50)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)

        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')
        #
        #
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # self.statusBar().showMessage('Ready')
        #
        # exitAction = QAction(QIcon('image.jpg'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('Exit application')
        # exitAction.triggered.connect(qApp.quit)
        #
        # # self.statusBar()
        #
        # self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))


        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        # filemenu = menubar.addMenu('&File')
        # filemenu.addAction(exitAction)


        #
        # self.toolbar = self.addToolBar('Exit')
        # self.toolbar.addAction(exitAction)
        # self.center()




        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())