import sys
import Bio.SeqIO
import gzip

# Check if the file argument is provided
if len(sys.argv) < 3:
    print('please provide a sequence files',file=sys.stderr)
    sys.exit(1)

#aa count for fasta
def aa_count_fasta(filename):
    aa_counts = {}
    fasta_total = 0
    seqfile = open(filename)
    for seq_record in Bio.SeqIO.parse(seqfile, "fasta"):
        seq = seq_record.seq
        for aa in seq:
            fasta_total += 1
            if aa in aa_counts:
                aa_counts[aa] += 1
            else:
                aa_counts[aa] = 1
    seqfile.close()

    most_freq = max(aa_counts, key=aa_counts.get)
    least_freq = min(aa_counts, key=aa_counts.get)

    print('AA counts', aa_counts)
    print('most frequent AA:', most_freq, aa_counts[most_freq])
    print('least frequent AA:', least_freq, aa_counts[least_freq])
    
    return aa_counts, fasta_total

#aa count fot swiss
def aa_count_swiss(filename):
    aa_counts = {}
    swiss_total = 0
    seqfile = open(filename)
    for seq_record in Bio.SeqIO.parse(seqfile, "uniprot-xml"):
        seq = seq_record.seq
        for aa in seq:
            swiss_total += 1
            if aa in aa_counts:
                aa_counts[aa] += 1
            else:
                aa_counts[aa] = 1
    seqfile.close()
    most_freq = max(aa_counts, key = aa_counts.get)
    least_freq = min(aa_counts, key = aa_counts.get)

    print('AA counts', aa_counts)
    print('most frequent AA:',most_freq, aa_counts[most_freq])
    print('least frequent AA:', least_freq, aa_counts[least_freq])

    return aa_counts, swiss_total

    
def compare_fasta_swissprot(fasta_counts, swissprot_counts, fasta_total, swiss_total):
    largest_diff = 0
    aa_largest_diff = ''
    
    for aa in fasta_counts:
        if aa in swissprot_counts:
            freq_fasta = fasta_counts[aa] / fasta_total
            freq_swissprot = swissprot_counts[aa] / swissprot_total
            
            diff = abs(freq_fasta - freq_swissprot)
            
            if diff > largest_diff:
                largest_diff = diff
                aa_largest_diff = aa

    print('Amino acid with largest difference in frequency:', aa_largest_diff, 'difference:', largest_diff)



#call and get result
fasta_filename = sys.argv[1]
swissprot_filename = sys.argv[2]
#call AA count
fasta_counts = aa_count_fasta(fasta_filename)
swissprot_counts = aa_count_swiss(swissprot_filename)
#call compare
compare_fasta_swissprot(fasta_counts, swissprot_counts, fasta_total, swiss_total)
    
    









    
    
    
    
    










