def count_AA_frequency(aa_sequence):
    single_letter_AA = {}
    
    for each_AA in aa_sequence:
        single_letter_AA[each_AA] = 0
        
    for every_AA in aa_sequence:
        single_letter_AA[every_AA] += 1
        
    return single_letter_AA
    

#Program to translate mRNA -> Protein

codon_table = {"UUU": "F","UUC":"F","UUA":"L","UUG":"L",
               "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
               "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
               "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
               "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
               "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
               "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
               "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
               "UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop",
               "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
               "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
               "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
               "UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",
               "CGU":"R","CGC":"R","CGA":"R","CGG":"R",
               "AGU":"S","AGC":"S","AGA":"R","AGG":"R",
               "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}


def translate(sequence,codon=3):                             #Function translate will take 2 parametere Sequence and codon. Codon by default is set to 3 because we are going to read codons (i.e in triplets) 
    seq_len = len(sequence)                                  #seq_len contains the length of the sequence
    protein = ""                                             #Initializing protein variable to an empty string
    for i in range(0,(seq_len-3),codon):                     #
        if sequence[i: i + codon] in codon_table:
            triplet = sequence[i:i + codon]
            protein += codon_table[triplet]            
        else:
            break
    return protein

  
  def check_start_codon(sequence,start_codon="AUG"):
    sequence_len = len(sequence)
    len_start_codon = len(start_codon)
    
    for i in range(0,sequence_len):
        if sequence[i: i + len_start_codon] == start_codon:
            return "Start Codon present at position: {0}".format(i)
    return False
  
  
  
  def check_stop_codon(sequence,stop_codon="UAG"):
    sequence_len = len(sequence)
    len_stop_codon = len(stop_codon)
    
    for i in range(0,sequence_len):
        if sequence[i:i + len_stop_codon] == stop_codon:
            return "Stop codon present at position : {}".format(i)
        else:
            False
