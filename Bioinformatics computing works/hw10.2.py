def nuc_count(seq):
    count = {}
    for nuc in seq:
        if nuc in count:
            count[nuc] += 1
        else:
            count[nuc] = 1

    freq = {}#empty dic to store frequencies of each nuc
    for nuc in 'ATGC':
        freq[nuc] = count[nuc]*100/len(seq)
    return freq

def NegSortKey(f):
    return -f[1]

freq = nuc_count('ATTTGGCGTCA')
nuc = list(freq.keys())
f = list(freq.values())
paired = zip(nuc,f)
#print(paired)
sorted_frequencies = sorted(paired, key=NegSortKey)
#print(sorted_frequencies)
for nuc, percentage in sorted_frequencies:
    print(nuc, ":", round(percentage,2), "%")

''' HW problem 10.2
Write a program to compute and output the frequency of each nucleotide 
in a DNA sequence using a dictionary.
Output the frequencies in most-occurrences to least-occurrences order.
'''


