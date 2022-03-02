# Function that will return the length of the given sequence
def sequence_length(sequence):
    check_length = len(sequence)
    return check_length

#Function that will count the number of nucleotides in a given sequnece and return the counts
    
def count_bases(sequences):
    base_dict = {}
    
    for bases in sequences:
        base_dict[bases] = 0
    for letter in sequences:
        base_dict[letter] += 1
    return base_dict
            
res = count_bases("ATGCATTTGGGGCCCAA")
print(res)

#Function that validates wether the given sequence is DNA sequence or not

def validate_nucleotides(sequence):
    nucleotides = ["A","T","G","C"]
    
    for base in sequence:
        if base not in nucleotides:
            return ("Nucleotide error {}".format(base))
    return sequence

res = validate_nucleotides("ATGC")
print(res)

#Function that will mimic the replication process in DNA (i.e returns its complementary bases)

def repliacte(sequence):
    complementary_bases = {"A":"T","G":"C","C":"G","T":"A"}
    repliacted = ""
    for base in sequence:
        transcribed_one += complementary_bases[base]
    return repliacted

res = repliacte("ATGCATGC")
print(res)

#Function that will transcribe DNA -> mRNA

def transcribe(sequence):
    complementary_base_pairs = {"A":"U","T":"A","G":"C","C":"G"}
    transcribed = ""
    liste = [complementary_base_pairs[bases] for bases in validate_nucleotides(sequence)]
    transcribed = transcribed.join(liste)
    return transcribed

#   return liste
res1 = transcribe("ATGC")
print(res1)

#Function that will return the number of matches and mismatches in a given sequence of equal sizes

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


#Function that will give you the AT composition in the given sequence

def AT_composition(sequence):
    count_AT = (((sequence.count('A') + sequence.count('T')) / len(sequence)) * 100)
    return count_AT

#Function that will give you the GC compositon in the given sequence


def GC_composition(sequence):
    count_GC = (((sequence.count('G') + sequence.count('C')) / len(sequence)) * 100)
    return count_GC

#Function that will return you the number of times AT pairs occurs in a given sequence

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


#Function that will give you the number of times GC pairs occurs in a given sequence

def GC_pairs(sequence,pattern="GC"):
    seq_len = len(sequence)
    pattern_len = len(pattern)
    gc_occurences = []
    
    for i in range(0,seq_len):
        if sequence[i : i + pattern_len] == pattern:
            gc_occurences.append(i)
    return gc_occurences

#Function Count will count the number of times a k-mer pattern appears as a substring of text

def count(text,pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        if text[i:i + pattern_len] == pattern:
            count = count + 1
    return count

res = count("","")
print(res)





