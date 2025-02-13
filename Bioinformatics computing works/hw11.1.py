#import
import sys
import csv
import math

#check command line arguments
if len(sys.argv)<3:
    print('There is a problem!')
    sys.exit(1)
          
data_file = sys.argv[1]
gene_name = sys.argv[2]

#read csv file
f = open(data_file)
rows = csv.DictReader(f)

#check if the gene name provided in commandline exists in dara_file header
if gene_name not in rows.fieldnames:
    print('wrong gene name')
    sys.exit(1)

expression_value = []
sample_type = {}

for r in rows:
    sample_category = r['TUMOUR'] #category
    expression = float(r[gene_name])
    expression_value.append(expression)

    if sample_category not in sample_type:
        sample_type[sample_category] = []
    sample_type[sample_category].append(expression)
#print(sample_type)

#calculate mean
def compute_mean(values):
    total = 0
    for value in values:
        total += value
    mean = total/len(values)
    return mean

#calculate standard deviation
def SD(values):
    mean = compute_mean(values)
    ss = 0
    for value in values:
        deviation = value - mean
        ss += math.pow(deviation,2)
    variance = ss/ (len(values)-1)
    std_dev = math.sqrt(variance)
    return std_dev

#calculate overall
def overall_mean_sd(expression_value):
    overall_mean = compute_mean(expression_value)
    overall_sd = SD(expression_value)
    print('overall mean for the gene:', round(overall_mean,2))
    print('overall standard deviation for the gene:', round(overall_sd,2))

#calculate mean and sd by category
def by_category(sample_type):
    for category, values in sample_type.items():
        mean = compute_mean(values)
        sd = SD(values)
        print('category',category,'mean',round(mean,2),'standard diviation', round(sd,2))

#call functions
overall_mean_sd(expression_value)
by_category(sample_type)


'''hw 11.1 question
Write a program that reads the microarray data in “data.csv” and computes the mean and standard deviation of the expression values of a specific gene overall, and within each sample category.
Get the name of the microarray datafile from the command-line.
Get the name of the gene from the command-line.
'''