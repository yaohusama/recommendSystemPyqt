#encoding=utf-8
import pandas as pd

data =['申论应试常用文体', '申论热点与实用知识', '申论五大应试能力提高策略', '五大模块题目']
relation=pd.read_csv("erec.csv", encoding="gbk")
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
print(entity_dict)
print(entity_child)
def get_path(item):
    if item not in res.keys():
        res[item]=item
    elif item not in entity_child.keys():
        res[item] = res[entity_dict[item]] + "->" + item
        return

    for item_each in entity_child[item]:
        # try:
        # print(entity_dict[item_each])
        # print(item)
        # print(item_each)
        res[item_each]=res[entity_dict[item_each]]+"->"+item_each
        # except:

        # print(item_each)
        get_path(item_each)
for item in data:
    get_path(item)

# for item in data:
#     res[item]=get_path(item)
print(res)