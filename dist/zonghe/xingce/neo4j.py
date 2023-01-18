#encoding=utf-8
import os
import json
import sys
d = os.path.dirname(__file__)
__path = os.path.dirname(d)
sys.path.append(__path) # 添加自己指定的搜索路径
from PyQt5.QtWebEngineWidgets import *

import py2neo
from PyQt5.QtGui import QIcon
d = os.path.dirname(__file__)
sys.path.append(d)
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ui_Form(object):
    def setupUi(self, Eletric):
        Eletric.setObjectName("Eletric")
        Eletric.resize(1314, 777)
        Eletric.setStyleSheet('''background:#e6e6fa;''')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Eletric.sizePolicy().hasHeightForWidth())
        Eletric.setSizePolicy(sizePolicy)
        self.table_sql = QtWidgets.QTableWidget(Eletric)
        self.table_sql.setGeometry(QtCore.QRect(330, 450, 771, 261))
        self.table_sql.setObjectName("table_sql")
        self.table_sql.setColumnCount(0)
        self.table_sql.setRowCount(0)
        self.widget = QtWidgets.QWidget(Eletric)
        self.widget.setGeometry(QtCore.QRect(30, 340, 281, 281))
        self.widget.setObjectName("widget")
        #
        # self.btnfanhui.setGeometry(QtCore.QRect(70, 200, 181, 56))
        # self.btnfanhui.setStyleSheet("QPushButton {\n"
        #                                "    border-radius: 8px;\n"
        #                                "    padding: 16px 32px;\n"
        #                                "    text-align: center;\n"
        #                                "    font: 10pt \"楷体\";\n"
        #                                "    text-decoration: none;\n"
        #                                "    font-size: 16px;\n"
        #                                "    margin: 4px 2px;\n"
        #                                "    background-color: white;\n"
        #                                "}")


        # self.groupBox = QtWidgets.QGroupBox(self.widget)
        # self.groupBox.setGeometry(QtCore.QRect(70,20,500, 1000))#141
        # font = QtGui.QFont()
        # font.setBold(False)
        # font.setWeight(50)
        # self.groupBox.setFont(font)
        # self.groupBox.setStyleSheet("")
        # self.groupBox.setObjectName("groupBox")
        # self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        # self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 500,1000))
        # self.layoutWidget.setObjectName("layoutWidget")
        # self.gridLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        # # self.gridLayout.setContentsMargins(100, 100, 100, 100)
        # self.gridLayout.setObjectName("gridLayout")
        self.btnfanhui = QtWidgets.QPushButton(Eletric)
        self.btnfanhui.setObjectName("btnfanhui")
        self.btnConfirms = QtWidgets.QPushButton(Eletric)
        # self.btnConfirms.setGeometry(QtCore.QRect(70, 270, 181, 56))
        #         self.btnConfirms.setStyleSheet("QPushButton {\n"
        # "    border-radius: 8px;\n"
        # "    padding: 16px 32px;\n"
        # "    text-align: center;\n"
        # "    font: 10pt \"楷体\";\n"
        # "    text-decoration: none;\n"
        # "    font-size: 16px;\n"
        # "    margin: 4px 2px;\n"
        # "    background-color: white;\n"
        # "}")
        self.btnConfirms.setObjectName("btnConfirms")
        self.btnfanhui.setStyleSheet('''
                color:White;
                    font:25px;
                    border-radius: 16px;
                    font-family:微软雅黑;
                    background:rgba(128,0,128,0.5);
                    border:1px;
                    opacity:0.5;
                    width:55px;''')
        self.btnConfirms.setStyleSheet('''color:White;
                    font:25px;
                    border-radius: 16px;
                    font-family:微软雅黑;
                    background:rgba(128,0,128,0.5);
                    border:1px;
                    opacity:0.5;
                    width:55px;''')
        # self.gridLayout.addWidget(self.btnConfirms)
        # self.gridLayout.addWidget(self.btnfanhui)
        self.labelTitle = QtWidgets.QLabel(Eletric)
        self.labelTitle.setGeometry(QtCore.QRect(50, 60, 219, 92))
        self.labelTitle.setStyleSheet("font: 20pt \"楷体\";\n"
"margin-left:auto;margin-right:auto;")
        self.labelTitle.setObjectName("labelTitle")
        self.Check_lineEdit = QtWidgets.QLineEdit(Eletric)
        self.Check_lineEdit.setGeometry(QtCore.QRect(30, 180, 271, 71))
        self.Check_lineEdit.setStyleSheet("QLineEdit {\n"
"    padding: 16px 32px;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    margin: 4px 2px;;\n"
"}")
        self.Check_lineEdit.setText("")
        self.Check_lineEdit.setObjectName("Check_lineEdit")
        self.btnConfirms_kg = QtWidgets.QPushButton(Eletric)
        self.btnConfirms_kg.setGeometry(QtCore.QRect(80, 650, 181, 56))
#         self.btnConfirms_kg.setStyleSheet("QPushButton {\n"
# "    border-radius: 8px;\n"
# "    padding: 16px 32px;\n"
# "    text-align: center;\n"
# "    font: 10pt \"楷体\";\n"
# "    text-decoration: none;\n"
# "    font-size: 16px;\n"
# "    margin: 4px 2px;\n"
# "    background-color: white;\n"
# "}")
        self.btnConfirms_kg.setObjectName("btnConfirms_kg")
        self.btnConfirms_kg.setStyleSheet('''
        color:White;
            font:25px;
            border-radius: 16px;
            font-family:微软雅黑;
            background:rgba(128,0,128,0.5);
            border:1px;
            opacity:0.5;
            width:55px;''')
        self.retranslateUi(Eletric)
        QtCore.QMetaObject.connectSlotsByName(Eletric)
        # button_qss = '''QMainWindow,Qwidget{background:#e6e6fa;}
        #     self.btnConfirms_kg{
        #     color:White;
        #     font:25px;
        #     border-radius: 16px;
        #     font-family:微软雅黑;
        #     background:rgba(128,0,128,0.5);
        #     border:1px;
        #     opacity:0.5;
        #     width:55px;
        # }
        # self.btnConfirms_kg:hover{
        #     background:#6666FF;
        # }
        # self.btnConfirms_kg:pressed{
        #     background:#6600FF;
        # }'''
        # Eletric.setStyleSheet(button_qss)

    def retranslateUi(self, Eletric):
        _translate = QtCore.QCoreApplication.translate
        Eletric.setWindowTitle(_translate("Eletric", "知识图谱"))
        # self.groupBox.setTitle(_translate("Eletric", "知识图谱的检索"))#_translate("Eletric", "基本操作")
        Eletric.setWindowIcon(QIcon(resource_path("xingce/static/pictures/icon.png")))
        self.btnConfirms.setText(_translate("Eletric", "确认"))
        self.btnfanhui.setText(_translate("Eletric","返回"))
        self.labelTitle.setText(_translate("Eletric", "实时检索"))
        self.btnConfirms_kg.setText(_translate("Eletric", "查看图谱"))
class MainWindow(QMainWindow, Ui_Form):  # 多重继承QMainWindow和Ui_MainWindow
    def __init__(self):
        super(MainWindow, self).__init__()  # 先调用父类QMainWindow的初始化方法
        self.setupUi(self)  # 再调用setupUi方法

    # 关闭当前界面, 打开主界面
    def toMainWindow(self):
        self.ui1 = MainWindow()
        self.ui1.show()
        self.ui1.close()
def getFiles(path, prefix):
    return [os.path.join(root, file) for root, dirs, files in os.walk(path) \
    for file in files if file.startswith(prefix)]

class search_return():
	"功能: 对数据库进行搜索操作\
	参数 search_name 为搜索名"
	def __init__(self,search_name):
		self.search_name = search_name
		self.graph = py2neo.Graph("http://localhost:7474",auth=("neo4j","m1891799"))


	def node(self):
		str1= "MATCH (n) WHERE id(n)=%d RETURN n"%(self.search_name)
		# str1 =  "MATCH(n{name:'%s'})RETURN n"%(self.search_name)
		return self.graph.run(str1).to_subgraph()

	def picture_path(self):
		path = os.path.dirname(os.path.dirname(d)) + "\\static\\pictures"
		return [os.path.abspath(os.path.join(root, file)) for root, dirs, files in os.walk(path) \
		    	for file in files if file.startswith(self.search_name)]

	def relationships(self,limit = 25):
		# str1 = "match(n{name: '%s'})-[r]-(b) RETURN r LIMIT %d"%(self.search_name,limit)
		str1 = "MATCH (n)-[r]-(b) WHERE id(n)=%d RETURN r LIMIT %d" % (self.search_name,int(limit))#id
		return self.graph.run(str1)

	def dict1(self):
		a = str(self.node()) #fuck neo4j
		# b=self.node().labels
		# print(self.node())
		# if str(self.node().labels)==':Run':
		# 	return self.dict_for_run()
		if self.node():
			dict_run=dict()
			dict_node=dict(self.node())
			str1="MATCH ()-[r]-b"
			dict_run['名称']=dict_node.pop('name')
			dict_run.update(dict_node)
			return dict_run
		else:
			return None


	def singleNode_json(self):
		node = self.node()
		a = str(node)  #fuck neo4j
		a = dict(node)
		a["id"] = node.identity
		a["label"]=str(node.labels)
		b=json.dumps({"nodes":[a],"links":[]},ensure_ascii=False)
		return b


	def dict_for_run(self):
		# print('start')
		dict_run = dict()

		relation_dict=dict()

		a = str(self.node())  # fuck neo4j
		# dict_run.update(dict(self.node()))
		dict_node = dict(self.node())
		dict_run['名称'] = dict_node.pop('name')
		dict_run.update(dict_node)

		str1 = "MATCH (n)-[r]-(b) WHERE id(n)=%d AND type(r)<>'故障后运行方式' RETURN n,r,b" % (self.search_name)
		result = self.graph.run(str1).to_subgraph()
		# for node in result.nodes:
		# 	id = node.identity
		# 	if (id == self.search_name):
		# 		dict_search = dict(node)
		# 		dict_search['name'+str(node.labels)]=dict_search.pop('name')
		# 		dict_run.update(dict_search)
		# 		print(dict_run)
		# 	str2 = "MATCH (n)-[r]-() WHERE id(n)=%d RETURN count(r)" % (id)
		# 	node_result = self.graph.run(str2).evaluate()
		# 	print(node_result)

		for relation in result.relationships:
			str1="MATCH ()-[r]->() WHERE id(r)=%d RETURN type(r)"%(relation.identity)
			relation_result=self.graph.run(str1).evaluate()
			# print(relation_result)
			str1="MATCH (n)-[r]->(b) WHERE id(r)=%d RETURN b"%(relation.identity)
			node_result = self.graph.run(str1).to_subgraph()
			str1= "MATCH (n)-[r]-() WHERE id(n)=%d RETURN count(r)" % (node_result.identity)
			relation_count=self.graph.run(str1).evaluate()
			if (relation_count>1):
				# print(relation_result)
				dict_node = dict(node_result)
				dict_node_name=dict()
				if relation_result in relation_dict.keys():
					i=relation_dict[relation_result]
					relation_result=relation_result+str(i)
					relation_dict[relation_result]=i+1
				else:
					relation_dict[relation_result]=2

				dict_node.pop('name')
				# dict_node_name[relation_result] = dict_node.pop('name')
				# dict_run.update(dict_node_name)
				dict_run.update(dict_node)

				dict_ex=dict()

				str1 = "MATCH (n)-[r]->(b) WHERE id(n)=%d RETURN n,r,b"%(node_result.identity)
				ex_result=self.graph.run(str1).to_subgraph()
				for ex_relation in ex_result.relationships:
					str1 = "MATCH ()-[r]->() WHERE id(r)=%d RETURN type(r)" % (ex_relation.identity)
					ex_relation_result = self.graph.run(str1).evaluate()
					# if ex_relation_result in relation_dict.keys():
					# 	i = relation_dict[ex_relation_result]
					# 	ex_relation_result = ex_relation_result + str(i)
					# 	relation_dict[ex_relation_result] = i + 1
					# else:
					# 	relation_dict[ex_relation_result] = 2
					str1 = "MATCH (n)-[r]->(b) WHERE id(r)=%d RETURN b" % (ex_relation.identity)
					ex_node_result = self.graph.run(str1).to_subgraph()
					ex_dict_node = dict(ex_node_result)
					ex_dict_node_name=dict()
					ex_dict_node_name[ex_relation_result] = ex_dict_node.pop('name')
					dict_ex.update(ex_dict_node_name)
					dict_ex.update(ex_dict_node)
					# dict_run.update(ex_dict_node_name)
					# dict_run.update(ex_dict_node)
				string=str(dict_ex)
				string=string.replace('\'','').replace('{','').replace('}','')
				dict_node_name[relation_result] = string
				dict_run.update(dict_node_name)

			else:
				dict_node=dict(node_result)
				dict_node_name = dict()
				if relation_result in relation_dict.keys():
					i=relation_dict[relation_result]
					relation_result=relation_result+str(i)
					relation_dict[relation_result]=i+1
				else:
					relation_dict[relation_result]=2
				dict_node_name[relation_result] = dict_node.pop('name')
				dict_run.update(dict_node_name)
				dict_run.update(dict_node)

		# print(dict_run)
		# print('end')

		# return dict(self.node()) if self.node() else None
		return dict_run



	def json(self):
		links = []
		nodes = []
		nodes_set = set()
		links_set = set()

		for record in self.relationships():
			link = record.to_subgraph()
			a = str(link)   # fuck py2neo
			# print('a',a)

			if link.start_node.identity not in nodes_set:
				dic = dict(link.start_node)
				dic['id'] = link.start_node.identity

				dic['label']=str(link.start_node.labels)

				nodes_set.add(link.start_node.identity)
				nodes.append(dic)
			if link.end_node.identity not in nodes_set:
				dic = dict(link.end_node)
				dic['id'] = link.end_node.identity

				dic['label'] = str(link.end_node.labels)

				nodes_set.add(link.end_node.identity)
				nodes.append(dic)

			if link.identity not in links_set:
				dic = dict(link)
				dic['relationships'] = type(link).__name__
				dic['id'] = link.identity
				dic['source'] = link.start_node.identity
				dic['target'] = link.end_node.identity
				links.append(dic)
				links_set.add(link.identity)

		# print(str(self.node().labels))
		if (str(self.node().labels)==':TS' or str(self.node().labels)==':TL'):
			nodes=[]
			links=[]

		a = json.dumps({"nodes" : nodes,"links" : links},ensure_ascii=False)
		return a


class channel_showNode(QObject):
    fromJS = pyqtSignal(str)
    toJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)

    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        print('showNode(%s) from Html' %strParameter)
        self.fromJS.emit(strParameter)

class channel_expandNode(QObject):
    fromJS = pyqtSignal(str)
    toJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)

    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        print('expandNode(%s) from Html' %strParameter)
        self.fromJS.emit(strParameter)

class channel_showPicPro(QObject):
    fromJS = pyqtSignal(str)
    toJS = pyqtSignal(str)
    def __init__(self, parent = None):
        super().__init__(parent)

    @pyqtSlot(str)
    def JSSendMessage(self, strParameter):
        print('showPicPro(%s) from Html' %strParameter)
        self.fromJS.emit(strParameter)


class neo4j(QtWidgets.QWidget):
    ToJS_showNode = pyqtSignal(str)
    ToJS_expandNode = pyqtSignal(str)
    #ToJS_showPicPro = pyqtSignal(str)
    def __init__(self, parent = None):

        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        graph = py2neo.Graph("http://localhost:7474", auth=("neo4j", "m1891799"))
        str1 = "MATCH (n:entity) RETURN n"
        result = graph.run(str1).to_subgraph()
        self.items_list=[]
        for s in list(result.nodes):
            self.items_list.append(dict(s).get('name'))
        self.ui.completer = QtWidgets.QCompleter(self.items_list)
        self.ui.completer.setFilterMode(Qt.MatchContains)
        self.ui.completer.setMaxVisibleItems(10)
        self.ui.Check_lineEdit.setCompleter(self.ui.completer)

        self.resize(QGuiApplication.primaryScreen().availableSize() );

        # self.defaultPicture = os.path.dirname(os.path.dirname(d)) + \
        # "\\now\\static\\pictures\\1.gif"

        self.__setlayout()

        # self.splitterV1.splitterMoved.connect(self.__pictureSizeChange)

        # self.splitter.splitterMoved.connect(self.__pictureSizeChange)

        # self.__draw(self.defaultPicture)


    def __setlayout(self):
        layout = QtWidgets.QHBoxLayout()
        self.splitterV1 = QtWidgets.QSplitter(self)
        self.splitterV1.setOrientation(Qt.Vertical)

        # self.splitterV1.addWidget(self.ui.SqlToolBox)
        self.splitterV1.addWidget(self.ui.labelTitle)
        self.splitterV1.addWidget(self.ui.Check_lineEdit)
        self.splitterV1.addWidget(self.ui.btnConfirms)
        self.splitterV1.addWidget(self.ui.btnfanhui)
        # self.splitterV1.addWidget(self.ui.btnConfirms_kg)
        self.splitterV1.addWidget(self.ui.widget)
        self.splitterV1.addWidget(self.ui.btnConfirms_kg)
        # self.splitterV1.setStretchFactor(0, 0)


        # self.splitterV1.setContentsMargins(5,5,5,5)
        # self.splitterV1.addWidget(self.ui.LabelWidget)
#        self.url = 'file:///' + os.path.dirname(os.path.dirname(d)) +\
 #       '/static/html/JSTest.html'

         #---Web widget and layout-------------------------
        self.browser = QWebEngineView(self)
        self.pWebChannel = QWebChannel(self.browser.page())

        self.browser_kg=QWebEngineView(self)
        self.browser_kg.setVisible(False)
        #------js和qt通信--------------------------




        self.channel_expandNode = channel_expandNode(self)
        self.pWebChannel.registerObject('channel_expandNode',self.channel_expandNode)

        self.channel_showNode = channel_showNode(self)
        self.pWebChannel.registerObject("channel_showNode",self.channel_showNode)

        self.channel_showPicPro = channel_showPicPro(self)
        self.pWebChannel.registerObject('channel_showPicPro',self.channel_showPicPro) 

        self.browser.page().setWebChannel(self.pWebChannel)

        #self.url = 'file:///F:/demo/now/static/html/JSTest.html'
        self.url = 'file:///' + (os.path.dirname(d)) +\
       '/xingce/static/html/show.html'
        # self.ur=resource_path("static/html/show.html")
        self.url = self.url.replace('\\','/')
        # print(self.url)
        self.browser.page().load(QUrl(self.url))
        self.browser.show()
        # self.browser.setVisible(False)
#------------------------------------------------------------------------------
       # self.url = 'file:///F:/demo/now`/static/html/JSTest.html'
        
        #self.url = self.url.replace('\\','/')
        #print("self.url = ",self.url)

        #self.browser = QWebEngineView()
        #self.browser.load(QUrl(self.url))
        
        self.splitterV2 = QtWidgets.QSplitter(self)
        self.splitterV2.setOrientation(Qt.Vertical)
        self.splitterV2.addWidget(self.browser)
        self.splitterV2.addWidget(self.ui.table_sql)
        self.splitterV2.addWidget(self.browser_kg)

        # self.splitterV2.setStretchFactor(0,20)
        # self.splitterV2.setStretchFactor(1,5)
        self.splitterV2.setSizes([1000,300])
        # self.browser.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        self.splitter = QtWidgets.QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal) 
        self.splitter.addWidget(self.splitterV1)
        self.splitter.addWidget(self.splitterV2)

        self.splitter.setStretchFactor(0,2)
        self.splitter.setStretchFactor(1,8)

        layout.addWidget(self.splitter)
        self.setLayout(layout)

        #---------------------------------


        self.channel_showNode.fromJS.connect(self.returnShowNode)
        self.ToJS_showNode.connect(self.channel_showNode.toJS)
        self.channel_expandNode.fromJS.connect(self.returnExpandNode)
        self.ToJS_expandNode.connect(self.channel_expandNode.toJS)

        self.channel_showPicPro.fromJS.connect(self.changePicPro)
        # self.ToJS_showPicPro.connect(self.channel_showPicPro.toJS)

    def changePicPro(self,strParameter):
        if not strParameter.isdigit():
            return
        strParameter=int(strParameter)
        # if not strParameter:
        #     return
        a = search_return(strParameter)
        print("changePicPro")
        # print(a.dict1())
        self.__createSearch(a.dict1())
        # self.__draw(a.picture_path())

    def returnShowNode(self,strParameter):
        if not strParameter.isdigit():
            return
        strParameter = int(strParameter)
        # if not strParameter:
        #     return
        a = search_return(strParameter)
        self.ToJS_showNode.emit(a.singleNode_json())

    def returnExpandNode(self,strParameter):
        if not strParameter.isdigit():
            return
        strParameter = int(strParameter)
        # if not strParameter:
        #     return
        a = search_return(strParameter)
        print("expandNode")
        self.ToJS_expandNode.emit(a.json())
        



#-------------------------------------------------------------
   
    def __draw(self, picture_path):
        if not picture_path:
            picture_path = self.defaultPicture
        else:
            picture_path = picture_path[0]
        self.ui.Picture.clear()
        pic = QPixmap(picture_path)
        self.ui.Picture.setPixmap(pic)


    def __pictureSizeChange(self):
        self.ui.Picture.resize(self.ui.LabelWidget.size())

    # def resizeEvent(self, event):
    #     self.ui.Picture.resize(self.ui.LabelWidget.size())
        

    def __createSearch(self, dic):
        self.ui.table_sql.setColumnCount(len(dic))
        self.ui.table_sql.setRowCount(1)
        self.ui.table_sql.setHorizontalHeaderLabels(dic.keys())
        self.ui.table_sql.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.table_sql.horizontalHeader().setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)

        i = 0
        for dictKey in dic.keys():
            newItem = QtWidgets.QTableWidgetItem(dic[dictKey])
            self.ui.table_sql.setItem(0,i,newItem)
            i += 1

    @pyqtSlot()
    def on_btnConfirms_kg_clicked(self):
        # self.splitterV2.setVisible(False)
        # self.browser.page().load()
        self.ui.table_sql.setVisible(False)
        self.browser.setVisible(False)
        self.browser_kg.setVisible(True)
        self.url = 'file:///' + d+ \
                   '/static/html/kg.html'
        # self.url=resource_path("static/html/kg.html")
        print(self.url)
        self.url = self.url.replace('\\', '/')
        self.browser_kg.page().load(QUrl(self.url))
        # self.browser.show()

    @pyqtSlot()
    def on_btnConfirms_clicked(self):
        # self.ui.table_sql.setVisible(True)
        # self.url='http://www.baidu.com'
        # self.url = 'file:///' + os.path.dirname(os.path.dirname(d)) + \
        #            '/static/html/show.html'
        # self.url = self.url.replace('\\', '/')
        # self.browser.page().load(QUrl(self.url))
        # self.browser.show()
        self.browser.setVisible(True)
        self.ui.table_sql.setVisible(True)
        self.browser_kg.setVisible(False)

        search_name1 = self.ui.Check_lineEdit.text()

        graph = py2neo.Graph("http://localhost:7474", auth=("neo4j", "m1891799"))
        str1 = "MATCH(n:entity) where n.name='%s' RETURN n" % (search_name1)
        result=graph.run(str1).to_subgraph()
        # print(len(result.nodes))
        if result==None:
            return
        if len(result.nodes)>1:
            return
        # print(result.identity)
        search_name=result.identity
        # a = str(result)  # fuck neo4j
        # neodict=dict(result) if result else None
        self.neo = search_return(search_name)
        tmp_dict={}
        import json
        res=json.loads(self.neo.json())
        node_dict = res['nodes']
        tmp_dict[str(search_name)]=search_name1
        for item in node_dict:
            tmp_dict[item["entity_id"]]=item["name"]
        if node_dict:
            self.__createSearch(tmp_dict)
            # self.__draw(self.neo.picture_path())
            self.ToJS_showNode.emit(self.neo.singleNode_json())
            # self.ToJS_expandNode.emit(self.neo.json())
            # self.browser.page().load(QUrl(self.url))




if __name__ == "__main__":
    import sys
    qapp = QtWidgets.QApplication(sys.argv)
    app = neo4j()
    app.show()
    sys.exit(qapp.exec_())