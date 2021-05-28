"""
Written by: Christopher Pondoc
This file creates the individual .csv file containing head sizes in one column
and the sex label ('0' or '1') in the other column. Used to provide data that is
readable under the `compare_sexes.m` script.
"""

# Helpfulf or parsing in data
import csv

"""
Gets data from the original .csv file to get head sizes and subject ids.
""" 
def get_data():
    subject_ids = []
    head_sizes = []
    with open('reference/svol.csv') as size_file:
        head_reader = csv.reader(size_file, delimiter=',')
        line_count = 0
        for row in head_reader:
            if line_count == 0:
                line_count += 1
            else:
                subject_ids.append(row[0])
                head_sizes.append(int(row[1]))
    return subject_ids, head_sizes

"""
Gets data from the original .csv file to get subject ids. and sexes
"""
def get_sexes(subject_ids):
    sexes = [None] * len(head_sizes)
    with open('reference/abcd_ssphp01.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (row[3] in subject_ids):
                index = subject_ids.index(row[3])
                if (row[7] == 'M'):
                    sexes[index] = 1
                else:
                    sexes[index] = 0
    return sexes

"""
Create .csv file with pertinent data.
"""
def create_file(head_sizes, sexes):
    with open('reference/sex_size.csv', mode='w') as sex_size_file:
        sex_size_writer = csv.writer(sex_size_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(sexes)):
            sex_size_writer.writerow([head_sizes[i], sexes[i]])

""" Run all pertinent functions """
if __name__ == '__main__':
    subject_ids, head_sizes = get_data()
    sexes = get_sexes(subject_ids)
    create_file(head_sizes, sexes)