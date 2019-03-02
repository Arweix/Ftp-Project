import sys
import resources
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtNetwork import QFtp
from PyQt4.QtCore import QFile, QIODevice
from PyQt4.QtGui import QMainWindow, QApplication, QIcon, QTreeWidgetItem
from FTP_interface import Ui_MainWindow

class FTP(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ftp = None
        self.back = self.up
        self.urlInfo = Qt.QUrlInfo()
        self.isDirectory = {}
        self.allfiles = self.treeWidget
        self.allfiles.setIconSize(QtCore.QSize(64, 64))
        self.allfiles.setHeaderHidden(True)
        self.font = QtGui.QFont()
        self.font.setFamily("MS Shell Dlg 2")
        self.font.setPointSize(18)
        self.progressDialog = QtGui.QProgressDialog(self)
        self.currentPath = ""
        self.download.setEnabled(False)
        self.font2 = QtGui.QFont()
        self.font2.setFamily("MS Shell Dlg 2")
        self.font2.setPointSize(10)
        self.status.setFont(self.font2)
        self.status.setText("Please enter the name of an FTP server.")
        self.allfiles.setFont(self.font)
        self.allfiles.setHeaderLabels(["Name", "Size", "Owner", "Group", "Time"])
        self.con.clicked.connect(self.connectOrDis)
        self.allfiles.itemActivated.connect(self.InFolder)
        self.progressDialog.canceled.connect(self.cancelDownload)
        self.back.clicked.connect(self.cdToParent)
        self.download.clicked.connect(self.down)
        self.allfiles.currentItemChanged.connect(self.enableDownloadButton)
        self.ftpserver.setText("ftp.ebi.ac.uk")

    def connectOrDis(self):
        if self.ftp:
            self.ftp.abort()
            self.ftp.deleteLater()
            self.ftp = None
            self.con.setText("Connect")
            self.status.setText("Disconnect")
            self.allfiles.setEnabled(False)
            self.download.setEnabled(False)
            self.setCursor(QtCore.Qt.ArrowCursor)
            return
        self.ftp = QFtp(self)
        self.setCursor(QtCore.Qt.WaitCursor)
        self.connectToFtp()

    def connectToFtp(self):
        self.ftp.commandFinished.connect(self.ftpCommandFinished)
        self.ftp.listInfo.connect(self.addToList)
        self.ftp.dataTransferProgress.connect(self.updateDataTransferProgress)
        self.allfiles.clear()
        self.allfiles.setEnabled(True)
        self.ftp.connectToHost(self.ftpserver.toPlainText())
        self.ftp.login()
        self.con.setText("Disconnect")
        self.status.setText("Connecting to FTP server %s..." % self.ftpserver.toPlainText())

    def ftpCommandFinished(self):
        self.setCursor(QtCore.Qt.ArrowCursor)
        if self.ftp.currentCommand() == QFtp.ConnectToHost:
            if self.ftp.error():
                self.con.setText("Connect")
                QtGui.QMessageBox.information(self, "FTP",
                                        "Unable to connect to the FTP server. Please check that the host name is correct.")
            self.status.setText("Logged onto %s." % self.ftpserver.toPlainText())
            self.download.setDefault(True)

        if self.ftp.currentCommand() == QFtp.Login:
            self.ftp.list()

        if self.ftp.currentCommand() == QFtp.Get:
            if self.ftp.error():
                self.status.setText("Canceled download of %s." % self.file.fileName())
                self.file.close()
                self.file.remove()
            else:
                self.status.setText("Downloaded %s to current directory." % self.file.fileName())
                self.file.close()

            del self.file
            self.progressDialog.hide()

    def cancelDownload(self):
        self.ftp.abort()


    def addToList(self, urlInfo):
        self.urlInfo = urlInfo
        self.item = QTreeWidgetItem()
        self.item.setText(0, self.urlInfo.name())
        self.item.setText(1, str(int(self.urlInfo.size())))
        self.item.setText(2, self.urlInfo.owner())
        self.item.setText(3, self.urlInfo.group())
        self.item.setText(4, self.urlInfo.lastModified().toString("dd.MM.yy"))

        self.pixmap = QIcon(":/images/folder.png" if self.urlInfo.isDir() else ":/images/file.png")
        self.item.setIcon(0, self.pixmap)

        self.isDirectory[self.urlInfo.name()] = self.urlInfo.isDir()
        self.allfiles.addTopLevelItem(self.item)
        if self.allfiles.currentItem():
            self.allfiles.setCurrentItem(self.allfiles.topLevelItem(0))


    def InFolder(self):
        self.name = str(self.allfiles.currentItem().text(0))
        if self.isDirectory.get(self.name):
            self.allfiles.clear()
            self.isDirectory.clear()
            self.currentPath += '/'
            self.currentPath += self.name
            self.ftp.cd(self.name)
            self.ftp.list()
            return

    def cdToParent(self):
        self.allfiles.clear()
        self.isDirectory.clear()
        idx = self.currentPath.rfind("/")
        if idx > 0:
            self.currentPath = self.currentPath[0: idx]
            self.ftp.cd(self.currentPath)
        else:
            self.currentPath = "/"
            self.ftp.cd("/")
        self.ftp.list()

    def updateDataTransferProgress(self, readBytes, totalBytes):
        self.progressDialog.setMaximum(totalBytes)
        self.progressDialog.setValue(readBytes)

    def down(self):
        try:
            self.fileName = self.allfiles.currentItem().text(0)
            if QFile.exists(self.fileName):
                QtGui.QMessageBox.information(self, "FTP",
                                              "There already exists a file called %s in "
                                              "the current directory." % self.fileName)
                return

            self.file = QFile(self.fileName)
            if not self.file.open(QtCore.QIODevice.WriteOnly):
                QtGui.QMessageBox.information(self, "FTP",
                                              "Unable to save the file %s." % self.fileName)

            self.ftp.get(self.allfiles.currentItem().text(0), self.file)

            self.progressDialog.setLabelText("Downloading %s..." % self.fileName)
            self.download.setEnabled(False)
            self.progressDialog.exec_()
        except AttributeError:
            QtGui.QMessageBox.information(self, "FTP",
                                          "No file selected")

    def enableDownloadButton(self):
        current = self.allfiles.currentItem()
        if current:
            currentFile = current.text(0)
            self.download.setEnabled(not self.isDirectory.get(currentFile))
        else:
            self.download.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    main = FTP()
    main.show()
    app.exit(app.exec_())

if __name__ == "__main__":
    main()