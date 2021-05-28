import csv
import numpy as np
def get_ids(fold_num):
    file_name = "/Users/cpondoc/Documents/qingyu_data/res/subject_ids/subid_" + str(fold_num) + ".txt" 
    subject_ids_file = open(file_name, mode='r')
    lines = subject_ids_file.readlines()
    subject_ids_file.close()
    subject_ids = []
    for line in lines:
        subject_ids.append(line[:-1])
    return subject_ids

def get_sexes(subject_ids):
    sexes = [None] * len(subject_ids)
    with open('/Users/cpondoc/Documents/qingyu_data/reference/abcd_ssphp01.csv') as all_info_file:
        csv_reader = csv.reader(all_info_file, delimiter=',')
        num_lines = 0
        for row in csv_reader:
            if num_lines <= 1:
                num_lines += 1
            else:
                for subject in subject_ids:
                    if (subject == row[4]):
                        cor_index = subject_ids.index(row[4])
                        sexes[cor_index] = row[7]
                num_lines += 1
        return sexes

def get_predictions(fold_num, flip):
    file_name = ""
    if (flip):
        file_name = "/Users/cpondoc/Documents/qingyu_data/res/prediction_flip/prediction_flip_" + str(fold_num) + ".txt" 
    else:
        file_name = "/Users/cpondoc/Documents/qingyu_data/res/predictions/prediction_" + str(fold_num) + ".txt" 
    prediction_file = open(file_name, mode='r')
    lines = prediction_file.readlines()
    prediction_file.close()
    predictions = []
    for line in lines:
        predictions.append(float(line))
    return predictions

def split_by_sex(sexes, predictions):
    male_scores = []
    female_scores = []
    for i in range(0, len(sexes)):
        if (sexes[i] == "M"):
            male_scores.append(predictions[i])
        else:
            female_scores.append(predictions[i])
    return male_scores, female_scores

import seaborn as sns
def plot_jitterplot(prediction, sex, type):
    prediction_np = np.array(prediction).astype(np.float)
    sns.set_theme(style="whitegrid")
    ax = sns.stripplot(y=prediction_np[:100]).set(title=sex + ' Prediction Scores (all Folds) - ' + type, ylabel='Prediction Score')

subject_ids = get_ids(1)
sexes = get_sexes(subject_ids)
predictions = get_predictions(1, False)
male_scores, female_scores = split_by_sex(sexes, predictions)
plot_jitterplot(male_scores, "Male", "1")

#print(sexes)