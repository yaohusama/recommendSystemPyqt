import numpy as np
import os
# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from datetime import datetime
import sys
import os
def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class mydatabase():
    conn = psycopg2.connect(database="postgres", user="postgres", password="0818", host="localhost", port="5432")
    cursor = conn.cursor()
    tmp = []
    # 查询的条件
    def rogatoryCondition(self,database="dataBase"):
        self.startTime =datetime(2019, 2, 4, 20, 44, 40)#yyyy-MM-dd hh:mm:ss2019-01-01 03:02:03
        self.endTime = datetime.now()
        print(self.endTime)
        self.dbName =database
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
                if j>0:
                    if isinstance(da[j],str):
                        tmp_list.append(da[j].strip())
                    else:
                        tmp_list.append(da[j])
            self.tmp.append(tmp_list)
        # print(self.tmp)
        return self.tmp

def load_data(args):
    n_user, n_item, train_data, eval_data, test_data = load_rating(args)
    n_entity, n_relation, kg = load_kg(args)
    print('data loaded.')
    predict_data=np.loadtxt(resource_path(args.dataset+"/predict_data.txt"),dtype=np.int32)
    return n_user, n_item, n_entity, n_relation, train_data, eval_data, test_data, kg,predict_data


def load_rating(args):
    print('reading rating file ...')

    # reading rating file
    rating_file = resource_path(args.dataset + '/ratings_final')
    rating_np = np.loadtxt(rating_file + '.txt', dtype=np.int32)
    f1=open(resource_path(args.dataset+"/predict_data.txt"),"r")
    tmp_num=len([item for item in f1.readlines() if len(item)>0])
    rating_np[:,1]=[item%tmp_num for item in rating_np[:, 1]]
    rating_np_shenlun = rating_np
    mydatabase1=mydatabase()
    rating_np_rm=np.array(mydatabase1.rogatoryCondition())
    rating_np_rm_shenlun=np.array(mydatabase1.rogatoryCondition("dataBase_shenlun"))
    if len(rating_np_rm)>len(rating_np):
        rating_np=rating_np_rm
        rating_np[:,1]=[item.split("->")[-1] for item in rating_np_rm[:,1]]
    if len(rating_np_rm_shenlun)>len(rating_np):
        rating_np_shenlun=rating_np_rm_shenlun
        rating_np_shenlun[:,1]=[item.split("->")[-1] for item in rating_np_rm_shenlun[:,1]]
    if args.dataset =="xingce":
        n_user = len(set(rating_np[:, 0]))#出现过的用户个数
        n_item = len(set([item for item in rating_np[:, 1]]))#出现过的电影个数
        train_data, eval_data, test_data = dataset_split(rating_np)
    else:
        n_user = len(set(rating_np_shenlun[:, 0]))  # 出现过的用户个数
        n_item = len(set([item for item in rating_np_shenlun[:, 1]]))  # 出现过的电影个数
        train_data, eval_data, test_data = dataset_split(rating_np_shenlun)

    return n_user, n_item, train_data, eval_data, test_data


def dataset_split(rating_np):
    print('splitting dataset ...')

    # train:eval:test = 6:2:2
    eval_ratio = 0.2
    test_ratio = 0.2
    n_ratings = rating_np.shape[0]

    eval_indices = np.random.choice(list(range(n_ratings)), size=int(n_ratings * eval_ratio), replace=False)
    left = set(range(n_ratings)) - set(eval_indices)
    test_indices = np.random.choice(list(left), size=int(n_ratings * test_ratio), replace=False)
    train_indices = list(left - set(test_indices))

    train_data = rating_np[train_indices]
    eval_data = rating_np[eval_indices]
    test_data = rating_np[test_indices]

    return train_data, eval_data, test_data


def load_kg(args):
    print('reading KG file ...')

    # reading kg file
    kg_file =  resource_path(args.dataset + '/kg_xtt')
    kg = np.loadtxt(kg_file + '.txt', dtype=np.int32)


    n_entity = len(set(kg[:, 0]) | set(kg[:, 2]))#两端的实体个数
    n_relation = len(set(kg[:, 1]))              #关系个数

    return n_entity, n_relation, kg