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


def validate_protein(protein):
    start_codon = "M"
    stop_codons = "Stop"
    
    if protein.startswith("M") and protein.endswith("Stop"):
        return protein
    else:
        return "Start codon error: {0}\n\t Stop codon error: {1}".format(start_codon,stop_codons)

def reading_frame(sequence,ORF,codon=3):
    sequence_len = len(sequence)
    protein = ""
    
    for i in range(ORF,sequence_len - codon + 1, codon):
        if sequence[i : i + codon] in codons:
            triplet = sequence[i : i + codon]
            protein += codons[triplet]
        else:
            break
    return validate_protein(protein)

res0 = reading_frame(sequence="AUGCGAUGA",ORF=0)
print("For ORF = 0 : %s" %(res0))
res1 = reading_frame(sequence="CGAGCCUAA",ORF=1)
print("For ORF = 1 : %s" %(res1))
res2 = reading_frame(sequence="CGAGCCUAG",ORF=2)
print("For ORF = 2 : %s" %(res2))

def count_gaps(seq1,seq2):
    
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    gaps = " "
    seq1_total_gaps = 0
    seq2_total_gaps = 0
    for i in range(len_seq1):
        if seq1[i] == gaps:
            seq1_total_gaps += 1

    for j in range(len_seq2):
        if seq2[j] == gaps:
            seq2_total_gaps +=1


    return seq1_total_gaps,seq2_total_gaps

gap1,gap2 = count_gaps("ATGCATGC","ACG TAG ATGC")
print("Gaps in seq1 = %d" %gap1,"\n" "Gaps in seq2 = %d" %gap2)


def common_substring(seq1,k_mer):
    seq1_len = len(seq1)
    possible_kmer_patterns = {}
    pattern_occurences = []
    
    for i in range(0,seq1_len-k_mer + 1):
        patterns = seq1[i : i + k_mer]
        if not patterns in possible_kmer_patterns:
            possible_kmer_patterns[patterns] = 0
        possible_kmer_patterns[patterns] += 1
    return possible_kmer_patterns
    
def count_common_pattern(res):
    biggest = 0
    for key,values in res.items():
        if values > biggest:
            biggest = values
            current_key = key
    return biggest,current_key

num,pat = count_common_pattern(common_substring("ATGCTGTGATGC",1))
print("Common substring is: %s" %(pat), "and number of times it occurs is: %d"%(num))



