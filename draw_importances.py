import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


feature_importances_df = pd.read_csv("decision_tree_importances.csv")

feature_importances_df  = feature_importances_df.sort_values(by=["Importance"], ascending=False)

feature_list = feature_importances_df["Feature"].to_list()[0: 8]
print(feature_list)

importance_array = feature_importances_df["Importance"].values[0: 8]

print(importance_array)


plt.figure(dpi=300)
plt.title("Features and Importances")#, fontsize=16)

plt.bar(range(len(importance_array)), importance_array)
plt.xticks(range(len(importance_array)), feature_list, rotation = 30, size="small")#, fontsize=12)

plt.xlabel('Feature')#, size='larger')
plt.ylabel('Importance')#, size='larger')

plt.grid()

for a,b in zip(range(len(importance_array)), importance_array):
    plt.text(a, b+0.01, '%.07f' % b, ha='center', va= 'bottom', rotation=30, size="small")#,fontsize=12)
    
plt.savefig('Figure_1_1.png',format='png')
plt.show()