with open("sequence.fasta","r") as f:
    file_handle = f.read()
    if not file_handle.startswith(">"):
        print("NOT A FASTA FILE")
    else:
        print(file_handle)


#Program to read FASTQ file

def readFASTQ(filename,mode):
    
    sequences = []
    qual_scores = []
    
    with open(filename,mode) as FASTQ:
        while True:
            FASTQ.readline()
            seq = FASTQ.readline().rstrip()
            FASTQ.readline()
            qualities = FASTQ.readline().rstrip()
            
            if len(seq) == 0 and len(qualities) == 0:
                break
            sequences.append(seq)
            qual_scores.append(qualities)
    return sequences,qual_scores

file = input()
modee = input()
seq,qual = readFASTQ(file,modee)
seq[:5]


def validate_megafile(f,m='r'):
    
    with open(f,m) as meg:
        mega_content = meg.read()
        
        if mega_content.startswith("#Mega"):
            return mega_content
        else:
            return "NOT A MEGA FILE"
        
res = validate_megafile('C:/Users/Srinath Ravichandran/Downloads/bioinfomethods1_labs_Lab3,4_sequences_prot_aligned.meg')
print(res)
