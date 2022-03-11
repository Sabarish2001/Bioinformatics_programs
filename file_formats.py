with open("sequence.fasta","r") as f:
    file_handle = f.read()
    if not file_handle.startswith(">"):
        print("NOT A FASTA FILE")
    else:
        print(file_handle)


#Program to read FASTQ file

def readFASTQ(filename, mode):

sequence = []
qual_scores = []

with open(filename,mode) as FASTQ:
while True:
FASTQ.readline() 
seq = FASTQ.readline() 
FASTQ.readline() 
qualities = FASTQ.readline() 
if len(seq) ==  0:
break

sequence.append(seq) 
qual_scores.append(qualities) 

return sequence, qual_scores


file = input() 
mode = input() 
seqs,quals = readFASTQ(file, mode) 
seqs[:5]
