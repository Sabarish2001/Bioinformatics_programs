with open("sequence.fasta","r") as f:
    file_handle = f.read()
    if not file_handle.startswith(">"):
        print("NOT A FASTA FILE")
    else:
        print(file_handle)
