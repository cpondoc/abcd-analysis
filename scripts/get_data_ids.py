"""
Written by: Christopher Pondoc
This file gets all of the corresponding data ids for the selected dataset
"""

# Helpful for parsing scripts
import csv

"""
Gets data from the original .csv file to get head sizes and subject ids.
""" 
def get_data():
    subject_ids = []
    head_sizes = []
    with open('../reference/svol.csv') as size_file:
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
Gets all of the head sizes and their corresponding z-scores
"""
def get_z_score(head_sizes):
    z_scores = [None] * len(head_sizes)
    with open('../reference/z_scores.txt') as z_scores_file:
        z_score_reader = csv.reader(z_scores_file)
        for row in z_score_reader:
            if (int(row[0]) in head_sizes):
                index = head_sizes.index(int(row[0]))
                z_scores[index] = float(row[1])
    return z_scores

"""
Gets the corresponding data set for matched pairs!
"""
def get_matched_pairs(z_scores, subject_ids, head_sizes):
    matched_ids = []
    matched_sizes = []
    matched_sexes = []
    with open('../reference/matched.txt') as matched_file:
        matched_reader = csv.reader(matched_file)
        for row in matched_reader:
            if (float(row[0]) in z_scores):
                index = z_scores.index(float(row[0]))
                matched_ids.append(subject_ids[index])
                matched_sizes.append(head_sizes[index])
                if (int(row[1]) == 1):
                    matched_sexes.append('M')
                else:
                    matched_sexes.append('F')
    return matched_ids, matched_sizes, matched_sexes

"""
Making the .csv for all of the data :) 
"""
def create_file(matched_ids, matched_sizes, matched_sexes):
    with open('../reference/matched_pairs.csv', mode='w') as matched_pairs_file:
        matched_pairs_writer = csv.writer(matched_pairs_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        matched_pairs_writer.writerow(['Subject ID', 'Head Size', 'Sex'])
        for i in range(0, len(matched_ids)):
            matched_pairs_writer.writerow([matched_ids[i], matched_sizes[i], matched_sexes[i]])

""" Run all pertinent functions """
if __name__ == '__main__':
    subject_ids, head_sizes = get_data()
    z_scores = get_z_score(head_sizes)
    matched_ids, matched_sizes, matched_sexes = get_matched_pairs(
        z_scores, subject_ids, head_sizes
    )
    create_file(matched_ids, matched_sizes, matched_sexes)

