def sequence_length(sequence):
    check_length = len(sequence)
    return check_length

with open("ebolaseq.txt",'r') as seq:
    res = sequence_length(seq.read())
    print("Length of the sequence = %s" %(res))
    
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
