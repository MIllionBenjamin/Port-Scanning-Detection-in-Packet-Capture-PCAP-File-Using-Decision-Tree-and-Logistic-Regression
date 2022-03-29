import pandas as pd
import numpy as np

for i in (4, 6):
    DT_result_df = pd.read_csv("test_result_decision_tree/after_preprocess_sample" + str(i) + ".csv")
    DT_result_labels = DT_result_df["label"].values
    print(DT_result_labels.shape)
    print(np.unique(DT_result_labels, return_counts=True))

    LR_result_df = pd.read_csv("test_result_logistic_regression/after_preprocess_sample"+ str(i) + ".csv")
    LR_result_labels = LR_result_df["label"].values
    print(LR_result_labels.shape)
    print(np.unique(LR_result_labels, return_counts=True))

    DT_0_LR_0_amount = 0
    DT_0_LR_1_amount = 0
    DT_1_LR_0_amount = 0
    DT_1_LR_1_amount = 0

    for j in range(0, len(DT_result_labels)):
        if DT_result_labels[j] == 0 and LR_result_labels[j] == 0:
            DT_0_LR_0_amount += 1
        if DT_result_labels[j] == 0 and LR_result_labels[j] == 1:
            DT_0_LR_1_amount += 1
        if DT_result_labels[j] == 1 and LR_result_labels[j] == 0:
            DT_1_LR_0_amount += 1
        if DT_result_labels[j] == 1 and LR_result_labels[j] == 1:
            DT_1_LR_1_amount += 1

    print(DT_0_LR_0_amount, DT_0_LR_1_amount, DT_1_LR_0_amount, DT_1_LR_1_amount)
    print(sum([DT_0_LR_0_amount, DT_0_LR_1_amount, DT_1_LR_0_amount, DT_1_LR_1_amount]))