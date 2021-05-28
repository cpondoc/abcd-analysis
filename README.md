# ABCD Data Analysis
Work with Dr. Qingyu Zhao at Stanford Computational Neuroscience Lab.

## Notebooks
- Correlation Graph: Contains info related to looking at the correlation between head size and sex.
- Box Plot: Contains info related to looking at the distribution of prediction scores. Making sure model does or does not need to be trained again.
- Accuracy Logger: Tracks all of the important metrics from the training of the network. Helpful for ensuring model works.

## Scripts
- `compare_sexes.m`: used to create the matched pairs training dataset, given all of the data points from the ABCD study. Modified by Chris Pondoc to add extra data regarding head size, so final histogram of head sizes of each gender transposed onto one another could be generated.
- `create_sex_size.py`: used to create the file that is fed into `compare_sexes.m` in order to be able to get the matched pairs dataset. Specifically, the script creates the individual .csv file containing head size in one column and the sex lable ('0' or '1') in the other column.
- `correct_correlation.py`: supplementary script used to visualize correlation, by splitting by sex, corresponding with the head sizes, and then viewing the jitter plot.