#计算河口氮与指标的相关度
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.stats import spearmanr

file = pd.read_csv("./middle_data/土壤河流氮数据.csv")
X_columns = file.columns[2:-11]
X_data = pd.DataFrame(file, columns=X_columns)
print(X_columns)
#非数值型数据编码
le = LabelEncoder()
X_data["LITHOLOGY"] = le.fit_transform(X_data["LITHOLOGY"])
X_data["DOMSOIL"] = le.fit_transform(X_data["DOMSOIL"])
X_data["企业规模"] = le.fit_transform(X_data["企业规模"])

y_data = file["总氮方差"]

for column in X_columns:
    print(column)
    print(spearmanr(X_data[column], y_data))
    print("_______________________________")
