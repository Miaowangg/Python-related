#Method 1 using dictionary to compute complement and using .append(), .reverse(), and ''.join()
def comp(nuc):
    d = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return d[nuc]

def reverseComp(seq):
    seq = seq.upper()
    rc_list = []

    for nuc in seq:
        rc_list.append(comp(nuc))
    rc_list.reverse()
    return ''.join(rc_list)

print(reverseComp('ATGC'))
print(reverseComp('CACTAGGTTGCGAAGCCTATGCTGATATAT'))
print(reverseComp('GGCTTTTACGTGCACCACCGCAGGCGGCTG'))
print(reverseComp('acaagggtctcacatcgagaaacaagacag'))
    
#Method 2 using for loop, if/elif, .insert(), and ''.join()
def reverseComp(seq):
    seq = seq.upper()
    rc_list = []
    for nuc in seq:
        if nuc == 'A':
            rc_list.insert(0,'T')
        elif nuc == 'T':
            rc_list.insert(0,'A')
        elif nuc == 'G':
            rc_list.insert(0,'C')
        elif nuc == 'C':
            rc_list.insert(0,'G')
    return ''.join(rc_list)
        
print(reverseComp('ATGC'))
print(reverseComp('CACTAGGTTGCGAAGCCTATGCTGATATAT'))
print(reverseComp('GGCTTTTACGTGCACCACCGCAGGCGGCTG'))
print(reverseComp('acaagggtctcacatcgagaaacaagacag'))

#Method 3 using s[i]=x(replace) and reversed()
def reverseComp(seq):
    seq_list = list(seq.upper())
    for i in range(len(seq_list)):
        if seq_list[i] == 'A':
            seq_list[i] = 'T'
        elif seq_list[i] == 'T':
            seq_list[i] = 'A'
        elif seq_list[i] == 'G':
            seq_list[i] = 'C'
        elif seq_list[i] == 'C':
            seq_list[i] = 'G'
    return ''.join(reversed(seq_list))

print(reverseComp('ATGC'))
print(reverseComp('CACTAGGTTGCGAAGCCTATGCTGATATAT'))
print(reverseComp('GGCTTTTACGTGCACCACCGCAGGCGGCTG'))
print(reverseComp('acaagggtctcacatcgagaaacaagacag'))

'''HW problem 8.1
Using just the concepts introduced so far, find as many (different!) ways as possible to code DNA reverse complement (at least 3!)
You may use any built-in function or string or list method.
You may use only basic data-types and lists and dictionaries.
Compare and critique each technique for robustness, speed, and correctness.
'''