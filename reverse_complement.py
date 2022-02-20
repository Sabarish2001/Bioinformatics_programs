def reverse_complement(sequence):
    my_complement = {'A':'T','T':'A','G':'C','C':'G'}
    reverse_complement = ""
    
    for seq in sequence:
        if seq in my_complement:
            reverse_complement += my_complement[seq]
    return reverse_complement[::-1]

pass_me_seq = input()
must_revcomp = reverse_complement(pass_me_seq)
print("rev = ",must_revcomp)
