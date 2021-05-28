# ABCD Data Analysis
Work with Dr. Qingyu Zhao at Stanford Computational Neuroscience Lab.

## Notebooks
- Correlation Graph: Contains info related to looking at the correlation between head size and sex.
- Box Plot: Contains info related to looking at the distribution of prediction scores. Making sure model does or does not need to be trained again.
- Accuracy Logger: Tracks all of the important metrics from the training of the network. Helpful for ensuring model works.

## Scripts
- `compare_sexes.m` -- used to create the matched pairs training dataset, given all of the data points from the ABCD study. Modified by Chris Pondoc to add extra data regarding head size, so final histogram of head sizes of each gender transposed onto one another could be generated.
- `correct_correlation.py` -- supplementary script used to visualize correlation, by splitting by sex, corresponding with the head sizes, and then viewing the jitter plot.