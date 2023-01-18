# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from datetime import datetime
class mydatabase():
    conn = psycopg2.connect(database="postgres", user="postgres", password="root", host="localhost", port="5432")
    cursor = conn.cursor()
    tmp = []
    # 查询的条件
    def rogatoryCondition(self):
        self.startTime =datetime(2019, 2, 4, 20, 44, 40)#yyyy-MM-dd hh:mm:ss2019-01-01 03:02:03
        self.endTime = datetime.now()
        print(self.endTime)

        self.dbName ="dataBase"
        self.select = "SELECT date, id ,line1 FROM {0} WHERE date > '{1}' and  date < '{2}'".format(#
            self.dbName,
            self.startTime,
            self.endTime)
        mydatabase.cursor.execute(self.select)
        self.data = mydatabase.cursor.fetchall()
        self.rowNum = len(self.data)  # 获取查询到的行数
        self.columnNum = len(self.data[0]) #获取查询到的列数
        user=0
        for i, da in enumerate( self.data):
            tmp_list=[user]
            for j in range(self.columnNum):
                tmp_list.append(da[j].strip())
            self.tmp.append(tmp_list)
        # print(self.tmp)
        return self.tmp
    # 查询输出
    # def dateSelect(self):
    #     self.condition = self.rogatoryCondition()
    #     try:
    #         mydatabase.cursor.execute(self.condition)
    #         self.data      = mydatabase.cursor.fetchall()
    #         self.rowNum    = len(self.data)  #获取查询到的行数
    #         self.columnNum = len(self.data[0]) #获取查询到的列数
    #
    #         self.dataView.setRowCount(self.rowNum)  #设置表格行数
    #         self.dataView.setColumnCount(self.columnNum)
    #
    #         for i, da in enumerate( self.data):
    #             for j in range(self.columnNum):
    #                 self.itemContent = QTableWidgetItem(( '%s' )  % (da[j]))
    #                 self.dataView.setItem(i,j,self.itemContent )
    #         self.alarmMessageBox("查询完成！")
    #     except Exception as exc:
    #         self.alarmMessageBox(str(exc))
    #          mydatabase.conn.commit()
if __name__ =="__main__":
    mydatabase=mydatabase()
    res=mydatabase.rogatoryCondition()
    data={"res":res}
    data=pd.DataFrame(data)
    data.to_csv("run.csv",encoding="utf-8")
    print(res)
# print(res)