#encoding=utf-8
import pandas as pd
data=pd.read_csv("entity.csv")
score_num={}
for index,item in enumerate(data["name"]):
    score_num[item]=index
print(list(score_num.keys()))
data=pd.read_csv("erec.csv", encoding="gbk")
f1=open("../mkr/shenlun/kg_xtt.txt", "w")
for item in zip(data["entity1"],data["entity2"]):
    if "；" not in item[1]:
        if len(item[1])==0:
            continue
        f1.write(str(score_num[item[0]])+"\t"+"0"+"\t"+str(score_num[item[1]])+"\n")
    else:
        tmp=item[1].split("；")
        for item_each in tmp:
            if len(item_each)==0:
                continue
            f1.write(str(score_num[item[0]]) + "\t" + "0" + "\t" + str(score_num[item_each]) + "\n")
f1.close()
f2=open("../mkr/shenlun/predict_data.txt", "w")
for item in range(len(score_num.keys())):
    f2.write("0\t"+str(item)+"\t0\n")
f2.close()