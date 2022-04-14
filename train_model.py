#训练模型
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

file = pd.read_excel("./middle_data/模型数据带空气.xlsx")
#X_columns = ["LITHOLOGY","dem","SLOPE_MED","DOMSOIL","Ph","平均氮肥","平均复合肥","平均农药","水系线密度","行业代码","企业规模","distance","NO2含量"]
X_columns = file.columns[8:-6]
X_data = pd.DataFrame(file, columns=X_columns)

#非数值型数据编码
le = LabelEncoder()
X_data["LITHOLOGY"] = le.fit_transform(X_data["LITHOLOGY"])
X_data["DOMSOIL"] = le.fit_transform(X_data["DOMSOIL"])
X_data["企业规模"] = le.fit_transform(X_data["企业规模"])

hangye_code = []
for i in range(0, len(X_data["行业代码"])):
    if type(X_data["行业代码"][i]) is str and len(X_data["行业代码"][i])>4:
        hangye_code.append(int(X_data["行业代码"][i][0:4]))
    else:
        hangye_code.append(int(X_data["行业代码"][i]))
X_data["行业代码"] = hangye_code
y_data = file["F0_5CM1"]
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.3)
#reg = ExtraTreesRegressor()
'''param_grid = {
    "n_estimators":[100,200,300,400,500,600,700,1000],
    "max_depth":[5,6,7,8,9,10,11,12,13,14,15]
}'''
#reg = RandomForestRegressor()
#search = GridSearchCV(reg, param_grid, scoring="r2", cv=10).fit(X_data, y_data)
##print("best parameters:", search.best_params_)


df = pd.DataFrame(None)
df["column_name"] = X_columns
for i in range(0, 3):
    reg1 = XGBRegressor(max_depth=8, n_estimators=100)
    reg1.fit(X_data, y_data)
    print(reg1.score(X_data,y_data))
    df[str(i)] = reg1.feature_importances_
df.to_csv("res_importance2.csv", index=False, encoding="gbk")
