import sys
def complement(seq):
    seq = seq.upper()
    nucleotides = 'ACGT'
    complements = 'TGCA'
    comp_seq = ''
    
    for nuc in seq:  
        i = nucleotides.find(nuc)
        if i >= 0:
            comp_seq += complements[i]
        else:
            comp_seq += nuc 
    
    return comp_seq

def reverseComplement(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

seq_file = sys.argv[1]
input_seq = open(seq_file)

for lines in input_seq:
    primers = lines.strip().split()
    if len(primers) >= 2:
        forward_primer = primers[0]
        reverse_primer = primers[1]
        print(reverseComplement(forward_primer), reverseComplement(reverse_primer))
    else:
        print('wrong primers')   
input_seq.close()

'''HW problem 7.1
Write a command-line program for computing the reverse complement of primer pairs:
Primer pairs are listed in a file, one per line.
Forward and reverse primers on each line are separated by a space. Ignore anything after the first two space separated “words” on each line.
e.g. Example input file: here
Print the reverse complement of each primer of the pair in the same format as the input file. 
Hint: Use open(…).read() to read the entire contents of the file into a string…
'''






