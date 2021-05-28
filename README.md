# ABCD Data Analysis
Work with Dr. Qingyu Zhao at Stanford Computational Neuroscience Lab.

## Introduction
- My research study involves examining data utilized for the publication “Deep learning identifies morphological determinants of sex differences in the pre-adolescent brain” and determining if the head size disparities amongst males and females was a confounding variable in the training of the CNN.
- Note: Males tend to have larger head sizes than females
- Given that there was a correlation, I then designed a machine learning algorithm to train on a matched pairs dataset, ensuring that the effect of the head size in training was mitigated.

## Notebooks
- Correlation Graph: Contains info related to looking at the correlation between head size and sex.
- Box Plot: Contains info related to looking at the distribution of prediction scores. Making sure model does or does not need to be trained again.
- Accuracy Logger: Tracks all of the important metrics from the training of the network. Helpful for ensuring model works.

## Scripts
- `compare_sexes.m`: used to create the matched pairs training dataset, given all of the data points from the ABCD study. Modified by Chris Pondoc to add extra data regarding head size, so final histogram of head sizes of each gender transposed onto one another could be generated.
- `create_sex_size.py`: used to create the file that is fed into `compare_sexes.m` in order to be able to get the matched pairs dataset. Specifically, the script creates the individual .csv file containing head size in one column and the sex lable ('0' or '1') in the other column.
- `get_data_ids.py`: used to get corresponding data ids for a selected dataset. Helper script!
- `split_training.py`: A hacky solution to parsing the data from the training results from the NN. Simply more of a sandbox file.
- `print_results.py`: Companion to graph results. Helper script!
- `correct_correlation.py`: supplementary script used to visualize correlation, by splitting by sex, corresponding with the head sizes, and then viewing the jitter plot.