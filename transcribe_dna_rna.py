#Transcribing DNA -> RNA

def transcribe_my_DNA(sequence):
    my_bases = {'A':'T','T':'U','G':'C','C':'G'}
    transcribed_seq = ""
    for seq in sequence:
        if seq in my_bases:
            transcribed_seq += my_bases[seq]
    return transcribed_seq
            
pass_me_DNA = input()
here_is_yourRNA = transcribe_my_DNA(pass_me_DNA)
print(here_is_yourRNA)
