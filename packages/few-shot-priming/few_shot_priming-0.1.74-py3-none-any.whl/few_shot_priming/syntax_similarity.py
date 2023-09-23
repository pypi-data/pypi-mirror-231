import fkassim.FastKassim as fkassim
import numpy as np
def calc_syntactic_similarity(df_test, df_training):
    similarities = np.zeros(((len(df_test),len(df_training))))
    FastKassim = fkassim.FastKassim(fkassim.FastKassim.LTK)
    for i, test_text in enumerate(df_test["text"]):
        for j, train_text in enumerate(df_training["text"]):
            similarity = FastKassim.compute_similarity(test_text, train_text)
            similarities[i, j] = similarity
    return similarities

def evaluate_similarity(experiment, arguments_to_check):