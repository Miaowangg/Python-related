def rc(seq):
    d = {'A':'T', 'T':'A', 'G':'C', 'C':'G','a':'t', 't':'a', 'c':'g', 'g':'c'}
    return ''.join(map(d.get, reversed(seq)))

print(rc('ATGC'))
print(rc('atgc'))
print(rc('ATATACGTCAGTCAGTCGACTACTGACACCTGCTACGAC'))
print(rc('cgtagctagctgactgtacgatcgt'))

''' HW problem 10.1
Write a reverse complement function (and package it up as a program)
as compactly as possible (1-2 lines), using the techniques introduced today.
'''