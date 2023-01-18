#encoding=utf-8
import pandas as pd

data = ['类比推理', '图形推理', '定义判断', '逻辑判断', '常识判断', '数量关系', '资料分析', '言语理解与表达']
relation=pd.read_csv("erec.csv",encoding="gbk")
entity_dict={}
entity_child={}
for item in zip(relation["entity1"],relation["entity2"]):
    if "；" not in item[1]:
        entity_dict[item[1]]=item[0]
        entity_child[item[0]]=[item[1]]
    else:
        tmp=item[1].split("；")
        # print(tmp)
        if item[0] not in entity_child.keys():
            entity_child[item[0]]=[]
        for item_each in tmp:
            entity_child[item[0]].append(item_each)
            entity_dict[item_each]=item[0]
            assert entity_dict[item_each]==item[0]
res= {}
# print(entity_dict)
# print(entity_child)
def get_path(item):
    if item not in res.keys():
        res[item]=item
    elif item not in entity_child.keys():
        res[item] = res[entity_dict[item]] + "->" + item
        return

    for item_each in entity_child[item]:
        # try:
        res[item_each]=res[entity_dict[item_each]]+"->"+item_each
        # except:

        # print(item_each)
        get_path(item_each)
for item in data:
    get_path(item)

# for item in data:
#     res[item]=get_path(item)
print(res)