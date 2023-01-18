import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from xingce.mygui import tree_test as tree
from xingce.mygui import Ui_MainWindow  # 由.UI文件生成.py文件后，导入创建的GUI类
from xingce.mygui import Ui_MainWindow_xingce as xingce1
from xingce.mygui import Ui_MainWindow_notfinished as not_finished
from xingce.mygui import Ui_MainWindow_studied as studied
from xingce.mygui import tree as choosed
from xingce.neo4j import  neo4j
from xingce.recom_view import MyMain as recom
from shenlun.mygui import tree_test as tree_shenlun
from shenlun.mygui import Ui_MainWindow as Ui_MainWindow_shenlum  # 由.UI文件生成.py文件后，导入创建的GUI类
from shenlun.mygui import Ui_MainWindow_xingce as xingce1_shenlun
from shenlun.mygui import Ui_MainWindow_notfinished as not_finished_shenlun
from shenlun.mygui import Ui_MainWindow_studied as studied_shenlun
from shenlun.mygui import tree as choosed_shenlun
from shenlun.neo4j import  neo4j as neo4j_shenlun
from shenlun.recom_view import MyMain as recom_shenlun
import os
def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class MainWindow(QMainWindow, Ui_MainWindow):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(MainWindow, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法

    # 关闭当前界面, 打开主界面
    def toMainWindow(self):
        self.ui1 = MainWindow()
        self.ui1.show()
        self.ui1.close()
class xingce1(QMainWindow, xingce1):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(xingce1, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
class not_finished(QMainWindow, not_finished):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(not_finished, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
class tree1(QWidget,tree):
    def __init__(self,num):
        super(tree1, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.tree(self,num=num)

# class recom_ui(QWidget, recom):
#     def __init__(self, num):
#         super(recom_ui, self).__init__()  # 先调用父类QMainWindow的初始化方法
#         # self.tree(self)
class choosed(QWidget,choosed):
    def __init__(self,num):

        super(choosed, self).__init__()  # 先调用父类QMainWindow的初始化方法

        self.tree(self,nu=num)
class studied(QMainWindow, studied):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(studied, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
class MainWindow_shenlun(QMainWindow, Ui_MainWindow_shenlum):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(MainWindow_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法

    # 关闭当前界面, 打开主界面
    def toMainWindow(self):
        self.ui1 = MainWindow()
        self.ui1.show()
        self.ui1.close()
class xingce1_shenlun(QMainWindow, xingce1_shenlun):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(xingce1_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
class not_finished_shenlun(QMainWindow, not_finished_shenlun):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(not_finished_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
class tree1_shenlun(QWidget,tree_shenlun):
    def __init__(self,num):
        super(tree1_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.tree(self,num=num)

# class recom_ui(QWidget, recom):
#     def __init__(self, num):
#         super(recom_ui, self).__init__()  # 先调用父类QMainWindow的初始化方法
#         # self.tree(self)
class choosed_shenlun(QWidget,choosed_shenlun):
    def __init__(self,num):

        super(choosed_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法

        self.tree(self,nu=num)
class studied_shenlun(QMainWindow, studied_shenlun):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(studied_shenlun, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    button_qss = '''QMainWindow,Qwidget{background:#e6e6fa;}

        QPushButton{
        color:White;
        font:25px;
        border-radius: 16px;
        font-family:微软雅黑;
        background:rgba(128,0,128,0.5);
        border:1px;
        opacity:0.5;
        width:55px;
    }
    QPushButton:hover{
        background:#6666FF;
    }
    QPushButton:pressed{
        background:#6600FF;
    }'''
    treea=tree1(num=1)
    treea.setWindowTitle("从高到低排序")
    treea.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    treed=tree1(num=0)
    treed.setWindowTitle("从低到高排序")
    treed.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    window = MainWindow()
    treea_shenlun = tree1_shenlun(num=1)
    treea_shenlun.setWindowTitle("从高到低排序")
    treea_shenlun.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    treed_shenlun = tree1_shenlun(num=0)
    treed_shenlun.setWindowTitle("从低到高排序")
    treed_shenlun.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    window.setStyleSheet(button_qss)
    xingce1=xingce1()
    xingce1.setStyleSheet(button_qss)
    studied=studied()
    studied.setStyleSheet(button_qss)
    choosedp=choosed(num=0)
    choosedp.setStyleSheet(button_qss)
    choosedn=choosed(num=1)
    choosedn.setStyleSheet(button_qss)
    xingce1_shenlun = xingce1_shenlun()
    xingce1_shenlun.setStyleSheet(button_qss)
    studied_shenlun = studied_shenlun()
    studied_shenlun.setStyleSheet(button_qss)
    choosedp_shenlun = choosed_shenlun(num=0)
    choosedp_shenlun.setStyleSheet(button_qss)
    choosedn_shenlun = choosed_shenlun(num=1)
    choosedn_shenlun.setStyleSheet(button_qss)
    window.show()
    not_finished=not_finished()
    not_finished.setStyleSheet(button_qss)
    neo4j=neo4j()
    recom_ui=recom()
    recom_ui.setvalue()
    recom_ui.setStyleSheet(button_qss)
    recom_p = recom()
    recom_p.setStyleSheet(button_qss)
    choosedn.setWindowTitle("已学习部分")
    choosedn.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    choosedp.setWindowTitle("未学习部分")
    choosedp.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    not_finished_shenlun = not_finished_shenlun()
    not_finished_shenlun.setStyleSheet(button_qss)
    neo4j_shenlun = neo4j_shenlun()
    recom_ui_shenlun = recom_shenlun()
    recom_ui_shenlun.setvalue()
    recom_ui_shenlun.setStyleSheet(button_qss)
    recom_p_shenlun = recom()
    recom_p_shenlun.setStyleSheet(button_qss)
    choosedn_shenlun.setWindowTitle("已学习部分")
    choosedn_shenlun.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    choosedp_shenlun.setWindowTitle("未学习部分")
    choosedp_shenlun.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
    window.pushButton.clicked.connect(
        lambda: {window.close(), xingce1.show()}
    )
    window.pushButton_2.clicked.connect(
        lambda: {window.close(), xingce1_shenlun.show()}
    )
    xingce1.pushButton_4.clicked.connect(
        lambda: {xingce1.close(), window.show()}
    )
    xingce1.pushButton.clicked.connect(
        lambda: {xingce1.close(), not_finished.show()}
    )
    xingce1_shenlun.pushButton_4.clicked.connect(
        lambda: {xingce1_shenlun.close(), window.show()}
    )
    xingce1_shenlun.pushButton.clicked.connect(
        lambda: {xingce1_shenlun.close(), not_finished_shenlun.show()}
    )
    not_finished.pushButton_4.clicked.connect(
        lambda: {not_finished.close(), xingce1.show()}
    )
    not_finished.pushButton.clicked.connect(
        lambda: {not_finished.close(), treea.show()}
    )
    not_finished.pushButton_2.clicked.connect(
        lambda: {not_finished.close(), treed.show()}
    )
    not_finished_shenlun.pushButton_4.clicked.connect(
        lambda: {not_finished_shenlun.close(), xingce1_shenlun.show()}
    )
    not_finished_shenlun.pushButton.clicked.connect(
        lambda: {not_finished_shenlun.close(), treea_shenlun.show()}
    )
    not_finished_shenlun.pushButton_2.clicked.connect(
        lambda: {not_finished_shenlun.close(), treed_shenlun.show()}
    )
    treea.button.clicked.connect(
            lambda: {treea.close(), not_finished.show()}
        )
    treed.button.clicked.connect(
        lambda: {treed.close(), not_finished.show()}
    )
    treea_shenlun.button.clicked.connect(
        lambda: {treea_shenlun.close(), not_finished_shenlun.show()}
    )
    treed_shenlun.button.clicked.connect(
        lambda: {treed_shenlun.close(), not_finished_shenlun.show()}
    )
    xingce1.pushButton_2.clicked.connect(
        lambda: {xingce1.close(), studied.show()}
    )
    studied.pushButton.clicked.connect(
        lambda: {studied.close(), choosedn.show()}
    )#
    studied.pushButton_2.clicked.connect(
        lambda: {studied.close(), choosedp.show()}
    )  #
    studied.pushButton_3.clicked.connect(
        lambda: {studied.close(), xingce1.show()}
    )
    xingce1_shenlun.pushButton_2.clicked.connect(
        lambda: {xingce1_shenlun.close(), studied_shenlun.show()}
    )
    studied_shenlun.pushButton.clicked.connect(
        lambda: {studied_shenlun.close(), choosedn_shenlun.show()}
    )  #
    studied_shenlun.pushButton_2.clicked.connect(
        lambda: {studied_shenlun.close(), choosedp_shenlun.show()}
    )  #
    studied_shenlun.pushButton_3.clicked.connect(
        lambda: {studied_shenlun.close(), xingce1_shenlun.show()}
    )
    choosedn.button.clicked.connect(
        lambda: {choosedn.close(), studied.show()}
    )
    choosedp.button.clicked.connect(
        lambda: {choosedp.close(), studied.show()}
    )
    choosedn_shenlun.button.clicked.connect(
        lambda: {choosedn_shenlun.close(), studied_shenlun.show()}
    )
    choosedp_shenlun.button.clicked.connect(
        lambda: {choosedp_shenlun.close(), studied_shenlun.show()}
    )
    xingce1.pushButton_3.clicked.connect(
        lambda: {xingce1.close(), neo4j.show()}
    )
    neo4j.ui.btnfanhui.clicked.connect(
        lambda: {neo4j.close(), xingce1.show()}
    )
    not_finished.pushButton_3.clicked.connect(
        lambda: {not_finished.close(), recom_ui.show()}
    )
    recom_ui.pushButton_3.clicked.connect(
        lambda: {recom_ui.close(), not_finished.show()}
    )
    xingce1_shenlun.pushButton_3.clicked.connect(
        lambda: {xingce1_shenlun.close(), neo4j_shenlun.show()}
    )
    neo4j_shenlun.ui.btnfanhui.clicked.connect(
        lambda: {neo4j_shenlun.close(), xingce1_shenlun.show()}
    )
    not_finished_shenlun.pushButton_3.clicked.connect(
        lambda: {not_finished_shenlun.close(), recom_ui_shenlun.show()}
    )
    recom_ui_shenlun.pushButton_3.clicked.connect(
        lambda: {recom_ui_shenlun.close(), not_finished_shenlun.show()}
    )
    resn=recom(res=choosedn.get_not_checked(choosedn.tmp,num=0))
    num=0
    choosedn.pushButton.clicked.connect(

        lambda: {choosedn.close(), resn.setvalue(res=choosedn.get_not_checked(choosedn.tmp,num=0)),resn.show()}#

            )

    resp=recom(res=choosedp.get_checked(choosedp.tmp,num=0))
    choosedp.pushButton.clicked.connect(

        lambda: {choosedp.close(),resp.setvalue(res=choosedp.get_checked(choosedp.tmp,num=0)),resp.show()}

    )
    resn.pushButton_3.clicked.connect(
        lambda: {resn.close(), studied.show()}
    )
    resp.pushButton_3.clicked.connect(
        lambda: {resp.close(), studied.show()}
    )
    resn_shenlun = recom_shenlun(res=choosedn_shenlun.get_not_checked(choosedn_shenlun.tmp, num=0))
    num = 0
    choosedn_shenlun.pushButton.clicked.connect(

        lambda: {choosedn_shenlun.close(), resn_shenlun.setvalue(res=choosedn_shenlun.get_not_checked(choosedn_shenlun.tmp, num=0)), resn_shenlun.show()}  #

    )

    resp_shenlun = recom_shenlun(res=choosedp_shenlun.get_checked(choosedp_shenlun.tmp, num=0))
    choosedp_shenlun.pushButton.clicked.connect(

        lambda: {choosedp_shenlun.close(), resp_shenlun.setvalue(res=choosedp_shenlun.get_checked(choosedp_shenlun.tmp, num=0)), resp_shenlun.show()}

    )
    resn_shenlun.pushButton_3.clicked.connect(
        lambda: {resn_shenlun.close(), studied_shenlun.show()}
    )
    resp_shenlun.pushButton_3.clicked.connect(
        lambda: {resp_shenlun.close(), studied_shenlun.show()}
    )
    sys.exit(app.exec_())


