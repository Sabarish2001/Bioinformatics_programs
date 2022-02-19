def consensus(Motifs):
    k = len(Motifs)
    consensus_string = ''
    count = countmotif(Motifs)

    for j in range(k):
        max = 0
        frequent_symbol = ''
        for symbol in 'ATGC':
            if count[symbol][j] > max:
                max = count[symbol][j]
                frequent_symbol = symbol
        consensus_string += frequent_symbol

    return consensus_string

def pseudocount(Motifs):
    k = len(Motifs)
    t = len(Motifs)

    count = {}

    for symbol in 'ATGC':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def countmotif(Motifs):

    k = len(Motifs)
    t = len(Motifs)

    count = {}

    for symbol in 'ATGC':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count



print(consensus(['AACGTA',
                 'CCCGTT',
                 'CACCTT',
                 'GGATTA',
                 'TTCCGG']))







