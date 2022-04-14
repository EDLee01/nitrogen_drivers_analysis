#按照规则联合剩余指标
import pandas as pd
import numpy as np

nitrogen_file = pd.read_csv("./original_Data/土壤氮数据部分.csv")
item_file = pd.read_excel("./原始数据/珠三角社会经济气象因子.xlsx")

item_city = item_file["城市"]
nitrogen_city = nitrogen_file["市"]
nitrogen_land_cover = nitrogen_file["land_cover"]

other_columns = ["年均降水量", "农业平均值", "林业平均值","牧业平均值","渔业平均值","一产占比变化值","二产占比变化值","三产占比变化值","牛平均","羊平均",
                 "猪平均","家禽平均","年均气温","年均最高温","年均最低温","GDP","一产平均值","二产平均值","三产平均值","人口增长率","NO2平均值"]

a = []
b = []
c = []
for i in range(0, len(nitrogen_land_cover)):
    if nitrogen_land_cover[i]==20:
        for j in range(0, len(item_city)):
            if item_city[j] in nitrogen_city[i]:
                a.append(item_file["平均氮肥使用量"][j])
                b.append(item_file["平均复合肥使用量"][j])
                c.append(item_file["平均农药撒施量"][j])
    else:
        a.append(0)
        b.append(0)
        c.append(0)

for column in other_columns:
    l = []
    for i in range(0, len(nitrogen_land_cover)):
        for j in range(0, len(item_city)):
            if item_city[j] in nitrogen_city[i]:
                l.append(item_file[column][j])
    nitrogen_file[column] = l

nitrogen_file["平均氮肥使用量"] = a
nitrogen_file["平均复合肥使用量"] = b
nitrogen_file["平均农药撒施量"] = c
nitrogen_file.to_csv("./middle_data/土壤氮数据.csv", index=False, encoding="gbk")
nitrogen_file.to_csv("./middle_data/土壤氮数据utf.csv", index=False)
