import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("PortScan_Begin_to_End_tshark_deltail_with_label.csv")

'''
label
0    1487956
1     162657
dtype: int64
'''
print(dataset.groupby('label').size())

label = dataset["label"]
features = dataset.drop(["label", "ip.src", "ip.dst"], axis=1)


array_X = features.values
print(features.columns)
print(array_X)

array_Y = label.values
train_X, test_X, train_Y, test_Y = train_test_split(array_X, array_Y, train_size = 0.2, random_state = 42, stratify = array_Y)



clf = LogisticRegression(max_iter=500)
import time
train_begin = time.time()
clf.fit(train_X, train_Y)
print(clf.score(test_X, test_Y))
print("Total Train Time:", time.time() - train_begin)
print(clf.get_params())


print(clf.coef_)
print(clf.intercept_)


coef_datafram = pd.DataFrame({
    "Feature": features.columns, 
    "Importance": clf.coef_[0]
})

coef_datafram.to_csv("logistic_regression_coef.csv", index=False)