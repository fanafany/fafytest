# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-09-02 12:35 '
import sys
from PyQt5 import QtWidgets, QtGui, QtCore, Qt

class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()

        # the path of the image
        self.imagePath = r'D:\fafytest\PyQt5\image\l4.jpg'

        self.initGui()

        self.window.setWindowTitle('Fanafany')
        self.window.setGeometry(750,310,300,500)#窗口显示位置以及大小
        # self.window.showMaximized()#窗体最大显示
        self.window.setStyleSheet("border:3px solid #4e4e4e; backgroud-color:#6e6e6e")
        self.window.show()
        sys.exit(self.app.exec_())

    #create a function to initialize the GUI
    def initGui(self):
        self.applyBtn = QtWidgets.QPushButton('Apply',self.window)
        self.applyBtn.setGeometry(160,420,120,30)
        self.applyBtn.setStyleSheet("background: #4e4e4e; color: #f7f7f7")

        self.cancelBtn = QtWidgets.QPushButton('Cancel', self.window)
        self.cancelBtn.setGeometry(20, 420, 120, 30)
        self.cancelBtn.setStyleSheet("background: #4e4e4e; color: #f7f7f7")

        #create the label that holds the selected image
        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(0,0,300,400)
        self.label.setStyleSheet("background-color: #ffffff")

        #the image
        self.image = QtGui.QImage(self.imagePath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)

        self.label.setPixmap(self.pixmapImage)
        self.label.setScaledContents(True)


#instantiate an object to the class mainwindow
main = MainWindow()

