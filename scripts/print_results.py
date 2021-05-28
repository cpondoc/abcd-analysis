import matplotlib.pyplot as plt
import numpy as np
import csv
with open('/Users/cpondoc/Documents/qingyu_data/scripts/fold_1_results.txt') as size_file:
    data = []
    head_reader = csv.reader(size_file, delimiter=',')
    line_count = 0
    for row in head_reader:
        if line_count == 0:
            line_count += 1
        else:
            data.append(row)

epochs = []
acc_numbers = []
first_test_accs = []
second_test_accs = []

for row in data:
    test_acc_index = row[1].find("Acc:")
    second_position = row[1][test_acc_index + 5:]
    next_ind = second_position.find(" ")
    first_test_acc = float(second_position[:next_ind])
    second_test_acc = float(second_position[next_ind + 1:])
    first_test_accs.append(first_test_acc)
    second_test_accs.append(second_test_accs)
    epoch_number = row[0].find(" ")
    acc_number = row[0].find("Acc:")
    epochs.append(float(row[0][0:epoch_number]))
    number = float(row[0][acc_number + 5:])
    acc_numbers.append(number)

def graph_vals():
    ref_np = np.array(epochs).astype(np.float)
    values_np = np.array(acc_numbers).astype(np.float)
    plt.figure()
    plt.scatter(ref_np, values_np)
    plt.title("Training Accuracy: Fold " + str(1))
    plt.xlabel("Epoch")