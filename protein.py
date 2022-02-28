def translate(sequence,codon=3):
    seq_len = len(sequence)
    protein = ""
    for i in range(0,seq_len,codon):
        if sequence[i: i + codon] in codon_table:
            triplet = sequence[i:i + codon]
            protein += codon_table[triplet]
    return protein


res = translate("AUGUUUUAG")
print(res)
