import pandas as pd

# read csv
df = pd.read_csv('proteomics.summary.tsv', sep='\t')
# count genes with at least 2 distinct peptides in all sample
all_samples = (df.min() >= 2).sum()

# count genes with at least 2 distinct peptides in at least one sample
any_sample = (df.max() >= 2).sum()

# Print the results
print("Number of genes with at least two distinct peptides in all samples:",all_samples)
print("Number of genes with at least two distinct peptides in at least one sample:",any_sample)

''' HW 15.1 problems:
Write a pandas-based program to 
determine the number of genes with at least two distinct peptides in all samples.
determine the number of genes with at least two distinct peptides in at least one sample.
Hint: Slide 21 contains the essential tricks
'''