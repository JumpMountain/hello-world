# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import os
print(os.getcwd())
sys.path.append(os.getcwd()+"/UI")
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
#导入designer工具生成的login模块
from exit import Ui_MainWindow
class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.exitbutton.clicked.connect(self.close)
        self.pushButton_10.clicked.connect(self.messeage)
        #添加退出按钮信号和槽。调用close函数
    def messeage(self):
        self.lineEdit.clear()
        self.lineEdit.setText("woshinibaba")
        QMessageBox.information(self,"biaoti","wenbenneirong:%s"%(self.lineEdit.text()),QMessageBox.Yes|QMessageBox.No)
if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
