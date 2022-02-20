def count_bases(seq):
    base_dict = {'A':0,'T':0,'G':0,'C':0}
    for bases in seq:
        if bases in base_dict:
            base_dict[bases] += 1
    return base_dict

result = count_bases(sample_DNA)
result
