import sys
codon_file = sys.argv[1]
seq_file = sys.argv[2]

def readcodons(codon_file):
    data = {}
    f = open(codon_file)
    for l in f:
        sl = l.split()
        key = sl[0]
        value = sl[2]
        data[key] = value

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

    return codons, init

def comp(nuc):
    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return d.get(nuc,'')

def reverseComp(seq):
    seq = seq.upper()
    newseq = ""
    for nuc in seq:
        newseq = comp(nuc) + newseq
    return newseq

def transFrame (seq, codons, frame):
    seq = seq.upper()
    seqlen = len(seq)
    aaseq = []
    for i in range (frame - 1, seqlen, 3):
        codon = seq[i:i+3]
        if len(codon) == 3: 
            aa = codons.get(codon,'X')
            aaseq.append(aa)
    return ''.join(aaseq)

def checkAA(codon,codons):
    codon = codon.upper()
    N = 'ATGC'
    AAs = set()
    for i in N:
        possible_codon  = codon[:2] + i
        AAs.add(codons.get(possible_codon,'-'))

    if len(AAs) == 1:
        return codons.get(possible_codon,'-')
    else:
        return 'X'

def allcodons(seq, codons,frame):
    seq = seq.upper()
    allaas = ''
    for i in range(frame -1,len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            allaas += checkAA(codon,codons)
    return allaas
    
#open seq file
f = open(seq_file)
seq = ''.join(f.read().split()).upper()

#forward translation frame
codons, inti = readcodons(codon_file)
print('Forward frame 1:',transFrame(seq, codons, 1))
print('Forward frmae 2:',transFrame(seq, codons, 2))
print('Forward frame 3:',transFrame(seq, codons, 3))
#reverse(comp) translation frame
reverse_seq = reverseComp(seq)
print('Reverse frame 1:', transFrame(reverse_seq, codons, 1))
print('Reverse frame 2:', transFrame(reverse_seq, codons, 2))
print('Reverse frame 3:', transFrame(reverse_seq, codons, 3))
#check how third position affect protein forward transFrame
print('checkAA f_frame 1:',allcodons(seq, codons,1))
print('checkAA f_frame 2:',allcodons(seq, codons,2))
print('checkAA f_frame 3:',allcodons(seq, codons,3))
#check how third postion affect protein reverse transFrame
print('checkAA r_frame 1:',allcodons(reverse_seq, codons, 1))
print('checkAA r_frame 2:',allcodons(reverse_seq, codons, 2))
print('checkAA r_frame 3:',allcodons(reverse_seq, codons, 3))

'''hw problem 9.1
Modify your DNA translation program to translate in each forward frame (1,2,3)
Modify your DNA translation program to translate in each reverse (complement) translation frame too.
Modify your translation program to handle 'N' symbols in the third position of a codon
If all four codons represented correspond to the same amino-acid, then output that amino-acid.
Otherwise, output 'X'.
'''