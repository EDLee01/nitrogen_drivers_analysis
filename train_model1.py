#计算河口氮与指标的相关度
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.stats import spearmanr
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor

file = pd.read_csv("./middle_data/土壤河流氮数据.csv")
X_columns = file.columns[3:-12]
print(X_columns)
X_data = pd.DataFrame(file, columns=X_columns)
#非数值型数据编码
le = LabelEncoder()
X_data["LITHOLOGY"] = le.fit_transform(X_data["LITHOLOGY"])
X_data["DOMSOIL"] = le.fit_transform(X_data["DOMSOIL"])
X_data["企业规模"] = le.fit_transform(X_data["企业规模"])
hangye_code = []
for data in X_data["行业代码"]:
    hangye_code.append(int(data))
X_data["行业代码"] = hangye_code
y_data = file["河口总氮均值"]
'''reg = xgb.XGBRegressor()
param_grid = {
    "n_estimators":[100,200,300,400,500,600,700,1000],
    "max_depth":[5,6,7,8,9,10,11,12,13,14,15]
}
#reg = RandomForestRegressor()
search = GridSearchCV(reg, param_grid, scoring="r2", cv=10).fit(X_data, y_data)
print("测试集准确度：", search.score(X_data, y_data))
print("best parameters:", search.best_params_)
print("_________________________")'''
df = pd.DataFrame(None)
df["column_name"] = X_columns
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.3)
for i in range(0, 3):
    reg1 = XGBRegressor(max_depth=8, n_estimators=100)
    reg1.fit(X_data, y_data)
    print(reg1.score(X_data,y_data))
    df[str(i)] = reg1.feature_importances_
df.to_csv("res_importance1.csv", index=False, encoding="gbk")
