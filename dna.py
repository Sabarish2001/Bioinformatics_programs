def sequence_length(sequence):
    check_length = len(sequence)
    return check_length

    
def count_bases(sequences):
    base_dict = {}
    
    for bases in sequences:
        base_dict[bases] = 0
    for letter in sequences:
        base_dict[letter] += 1
    return base_dict
        

res = count_bases("ATGCATTTGGGGCCCAA")
print(res)

def validate_nucleotides(sequence):
    nucleotides = ["A","T","G","C"]
    
    for base in sequence:
        if base not in nucleotides:
            return ("Nucleotide error {}".format(base))
    return sequence

res = validate_nucleotides("ATGC")
print(res)

def repliacte(sequence):
    complementary_bases = {"A":"T","G":"C","C":"G","T":"A"}
    repliacted = ""
    for base in sequence:
        transcribed_one += complementary_bases[base]
    return repliacted

res = repliacte("ATGCATGC")
print(res)

def transcribe(sequence):
    complementary_base_pairs = {"A":"U","T":"A","G":"C","C":"G"}
    transcribed = ""
    liste = [complementary_base_pairs[bases] for bases in validate_nucleotides(sequence)]
    transcribed = transcribed.join(liste)
    return transcribed

#   return liste
res1 = transcribe("ATGC")
print(res1)

def match_mismatch(sequence_1,sequence_2):
    
    match = 0
    mismatch = 0
    
    if len(sequence_1) == len(sequence_2):
        for base in range(len(sequence_1)):
            if sequence_1[base] == sequence_2[base]:
                 match += 1            
            else:
                mismatch += 1
    
    return (match,mismatch)
    

x = match_mismatch(sequence_1="ATGCATGC",sequence_2="TTGCGTGC")
print("Matches = %s , Mismatches = %s" %(x))


def AT_composition(sequence):
    count_AT = (((sequence.count('A') + sequence.count('T')) / len(sequence)) * 100)
    return count_AT

    
def GC_composition(sequence):
    count_GC = (((sequence.count('G') + sequence.count('C')) / len(sequence)) * 100)
    return count_GC


def AT_pairs(sequence,pattern = "AT"):
    
    seq_len = len(sequence)
    pattern_len = len(pattern)
    occurences = []
    res = [occurences.append(i) for i in range(0,seq_len-1) if sequence[i: i + pattern_len] == pattern] 
    return occurences

                    #or
    
#    for i in range(0,(seq_len-1)):
#        if sequence[i: i + pattern_len] == pattern:
#            occurences.append(i)
#    return occurences


def GC_pairs(sequence,pattern="GC"):
    seq_len = len(sequence)
    pattern_len = len(pattern)
    gc_occurences = []
    
    for i in range(0,seq_len):
        if sequence[i : i + pattern_len] == pattern:
            gc_occurences.append(i)
    return gc_occurences





