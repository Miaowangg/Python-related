import sys
codon_file = sys.argv[1]
seq_file = sys.argv[2]

f = open(codon_file)
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
f.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

f = open(seq_file)

seq = ''.join(f.read().split())
f.close()
seqlen = len(seq)
aaseq = []
for i in range(0,seqlen,3):
    codon = seq[i:i+3]
    aa = codons[codon]
    aaseq.append(aa)
print(''.join(aaseq))

initial_codon = seq[:3]

if initial_codon in init and init[initial_codon]:
    print('The initial codon is consistent with the codon tables start codons')
else:
    print('The initial codon is not consistent with the codon tables start codons')
    

'''HW problem 8.2
Write a program that takes a codon table file (such as standard.code from the lecture) 
and a file containing nucleotide sequence (anthrax_sasp.nuc) as command-line arguments, 
and outputs the amino-acid sequence.
Modify your program to indicate whether or not the initial codon
is consistent with the codon table's start codons.
Use NCBI's taxonomy resource to look up and download the correct codon table 
for the anthrax bacterium. Re-run your program using the correct codon table. 
Is the initial codon of the anthrax SASP gene a valid translation start site?
'''

























