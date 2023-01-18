#encoding=utf-8
import pandas as pd
f2=open("erec.csv", "w", encoding="gbk")
with open("shenlun/erec_old.csv", encoding="gbk") as f1:
    res=f1.readlines()
    for item in res:
        tmp=item[1:-4]
        tmp_str=tmp.split()
        print(len(tmp_str))
        if len(tmp_str)<3:
            print(tmp_str)
            f2.write(tmp_str[0] + "," + "包括" + "," + tmp_str[1] + "," + "\n")
            continue
        f2.write(tmp_str[0]+","+tmp_str[1]+","+tmp_str[2]+","+"\n")
        # print(tmp_str[0]+","+tmp_str[1]+","+tmp_str[2]+","+"\n")
    print(res)
f2.close()