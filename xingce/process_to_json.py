import json
# coding=utf-8
# with open("erec_old.csv",encoding="utf-8") as f:
#     data=f.read()
#     print(data)
import pandas as pd
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
data=pd.read_csv("erec.csv",encoding="gbk")
dict_chid={}
vis={}
for item in zip(data["entity1"],data["entity2"]):
    dict_chid[item[0]]=[ item for item in str(item[1]).split("；") if len(item)>0]
def fx(item):
    res_dict = {}
    res_dict["content"] = item
    # if item not in vis.keys():
    vis[item]=1

    res_dict["children"] = []
    for item1 in dict_chid[item]:
        if item1 in dict_chid.keys():
            res = {}
            res["content"] = item1
            res["children"] = fx(item1)
            res_dict["children"].append(res)
        else:
            vis[item1]=1
            res_dict["children"].append(item1)



    return res_dict["children"]
total=[]
for item in zip(data["entity1"],data["entity2"]):
    if item[0] not in vis.keys():
        vis[item[0]]=0
    if vis[item[0]]==0:
        tmp={}
        tmp["content"]=item[0]
        tmp["children"]=fx(item[0])
        total.append(tmp)
    # res_dict["chidren"]=dict_chid[item[0]]
# newjson=json.dumps(total,ensure_ascii=False)
t={}
t["content"]="行测"
t["children"]=total
fp=open("data.json","w",encoding="utf-8")
fp.write(json.dumps(t,ensure_ascii=False))
fp.close()
# json.dump(total,open("data.json","w",encoding="utf-8"))
print(total)
#前提条件是父节点包含子节点应出现在最前面
