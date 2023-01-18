import os
import csv
import hashlib


def get_md5(string):
    """Get md5 according to the string
    """
    byte_string = string.encode("utf-8")
    md5 = hashlib.md5()
    md5.update(byte_string)
    result = md5.hexdigest()
    return result

dic=dict()
len_al=0
def build_entity(executive_ere, executive_import):
    """Create an 'executive' file in csv format that can be imported into Neo4j.
    format -> entity_id:ID,name,:LABEL
    label -> entity
    """
    print('Writing to {} file...'.format(executive_import.split('/')[-1]))
    xx=set()
    label=set()
    res=[]
    tmp_file=open(executive_import, 'r', encoding='utf-8')
    with open(executive_ere, 'r', encoding='gbk') as file_ere, \
        open(executive_import, 'a+', encoding='utf-8') as file_import:
        file_prep_csv = csv.reader(file_ere, delimiter=',')
        file_import_csv = csv.writer(file_import, delimiter=',')

        # headers = ['entity_id:ID', 'name', ':LABEL']
        # file_import_csv.writerow(headers)
        # print([item.strip("\n") for item in tmp_file.readlines() if len(item.strip("\n"))>0])
        global len_al
        len_al=len([item.strip("\n") for item in tmp_file.readlines() if len(item.strip("\n"))>0])
        for i, row in enumerate(file_prep_csv):
            if i == 0 or len(row) < 3:
                continue
            for indx,item in enumerate(row):
                if indx==1:
                    continue
                if indx==2:
                    if "；" in row[indx]:
                        tmp=str((item.strip())).split("；")
                        for itemx in tmp:
                            info = [itemx]
                            # info = [row[0], row[1], row[2]]
                            # # generate md5 according to 'name' 'gender' and 'age'
                            if itemx not in dic.keys():
                                dic[itemx]=len(dic)
                            # info_id = get_md5('{}'.format(itemx))
                                info_id=dic[itemx]
                                info.insert(0, info_id+len_al)
                                if len(itemx)==0:
                                    continue
                                res.append(itemx)
                                info.append("entity_shenlun")
                                file_import_csv.writerow(info)

                            if info_id not in xx:
                                # file_import_csv.writerow(info)
                                xx.add(info_id)
                        continue
                info=[item]
            # info = [row[0], row[1], row[2]]
            # # generate md5 according to 'name' 'gender' and 'age'
                if item not in dic.keys():
                    dic[item] = len(dic)
                    # info_id = get_md5('{}'.format(itemx))
                    info_id = dic[item]
                    info.insert(0, info_id+len_al)
                    info.append("entity")
                    if len(item)==0:
                        continue
                    res.append(item)
                    file_import_csv.writerow(info)
                # info_id = get_md5('{}'.format(item))
                # info.insert(0, info_id)
                # info.append("entity")
                # if info_id not in xx:
                #     file_import_csv.writerow(info)
                #     xx.add(info_id)
    print(res)
    tmp_file.close()
    print('- done.')




def build_relative(executive_ere, relation_import):
    """Create an 'executive_stock' file in csv format that can be imported into Neo4j.
    format -> :START_ID,title,:END_ID,:TYPE
               person          stock
    type -> employ_of
    """

    # len_al=len([item for item in tmp_file.readlines() if len(item) > 0])
    tmp_file = open(relation_import, 'r', encoding='utf-8')
    with open(executive_ere, 'r', encoding='gbk') as file_ere, \
        open(relation_import, 'a+', encoding='utf-8') as file_import:
        file_prep_csv = csv.reader(file_ere, delimiter=',')
        file_import_csv = csv.writer(file_import, delimiter=',')
        # len_al = len([item for item in tmp_file.readlines() if len(item) > 0])
        # headers = [':START_ID',  ':END_ID', ':TYPE']
        # file_import_csv.writerow(headers)
        for i, row in enumerate(file_prep_csv):
            if i == 0:
                continue
            # for item in row:
            # generate md5 according to 'name' 'gender' and 'age'
            if len(row)==0:
                continue
            if "；" in row[2]:
                item=row[2]
                tmp = str((item.strip())).split("；")
                # print(tmp)
                for itemx in tmp:
                    # start_id = get_md5('{}'.format(row[0]))
                    # end_id = get_md5('{}'.format(itemx))  # code
                    if len(itemx)==0:
                        continue
                    start_id=dic[row[0]]
                    end_id=dic[itemx]
                    relation = [start_id+len_al, end_id+len_al, "包括（申论）"]
                    file_import_csv.writerow(relation)
                    # print(relation)

                continue
            # start_id = get_md5('{}'.format(row[0]))
            # end_id = get_md5('{}'.format(row[2])) # code
            if len(row[2])!=0:
                start_id = dic[row[0]]
                end_id = dic[row[2]]
                relation = [start_id+len_al, end_id+len_al, "包括（申论）"]
                file_import_csv.writerow(relation)




if __name__ == '__main__':
    build_entity('erec.csv', '../xingce/entity.csv')
    build_relative('erec.csv', '../xingce/relation.csv')

