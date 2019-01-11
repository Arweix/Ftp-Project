import sys
import resources
from PyQt4 import QtCore, QtGui, Qt
import pyftp
from PyQt4.QtGui import QMainWindow, QApplication, QListWidgetItem, QIcon
from FTP_interface import Ui_MainWindow

class FTP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ftp = pyftp
        self.allfiles = self.treeWidget
        self.allfiles.setIconSize(QtCore.QSize(64, 64))
        self.font = QtGui.QFont()
        self.font.setFamily("MS Shell Dlg 2")
        self.font.setPointSize(20)
        self.allfiles.setFont(self.font)
        self.allfiles.setHeaderLabels(["Name", "Size", "Owner", "Group", "Time"])
        self.con.clicked.connect(self.connectOrDis)

    def connectOrDis(self):
        # if self.ftp.connect():
        #     self.ftp.close()
        #     self.con.setText("Connect")
        # else:
            self.ftp.connect()
            self.con.setText("Disconnect")





def main():
    app = QApplication(sys.argv)
    main = FTP()
    main.show()
    app.exit(app.exec_())

if __name__ == "__main__":
    main()