import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree 


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


clf = tree.DecisionTreeClassifier()
import time
train_begin = time.time()
clf = clf.fit(train_X, train_Y)
print("Total Train Time:", time.time() - train_begin)
result = clf.score(test_X, test_Y)


print(result)
print(clf.feature_importances_)



feature_importances_datafram = pd.DataFrame({
    "Feature": features.columns, 
    "Importance": clf.feature_importances_
})

feature_importances_datafram.to_csv("decision_tree_importances.csv", index=False)





import matplotlib.pyplot as plt

from sklearn import tree

plt.figure(dpi=300)
tree.plot_tree(clf, feature_names=features.columns,filled=True)  

plt.savefig('tree.png',format='png')
plt.show()
'''

# draw tree
'''
import graphviz
tree.plot_tree(clf)  
dot_data = tree.export_graphviz(clf, out_file="tree_graph.dot", 
                                feature_names=features.columns,  
                                class_names=True,  
                                filled=True, 
                                rounded=True,  
                                special_characters=True)  
graph = graphviz.Source(dot_data)  
#print(graph)

plt.show()

# draw_importance