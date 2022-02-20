def PatternCount(Text,Pattern):  #Pattern is a most frequent k-mer that appears in a string
    count = 0
    t = len(Text)
    k = len(Pattern)
    for i in range(t - k + 1):
        if Text[i : i + k] == Pattern:
            count += 1
    return count

def FrequencyMap(Text,k):
    frequency = {}
    t = len(Text)

    for i in range(t - k + 1):
        pattern = Text[i: i + k]
        frequency[pattern] = 0
        for i in range(t - k + 1):
            if Text[i: i + k] == pattern:
                frequency[pattern] += 1
    return frequency

#FrequentWords will return a key whose corresponding value equals the maximum

def FrequentWords(Text,k):
    words = []
    freq = FrequencyMap(Text,k)
    maxi = max(freq.values())
    for key in freq:
        if freq[key] == maxi:
            pattern = key
            words.append(pattern)
    return words

def Reverse(pattern):
    reverse_string = ''
    for i in pattern:
        reverse_string +=i
    return reverse_string[::-1]

def Complement(pattern):
    base_complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    res = [base_complements[base] for base in pattern]
    return "".join(res)



def ReverseComplement(Text):
    text = Complement(Text)
    text = Reverse(text)
    return text


def PatternMatching(Genome,Pattern):
    positions = []

    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i: i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def SymbolArray(Genome,symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0: n // 2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i: i+(n//2)], symbol)
    return array


def SkewArray(Genome):
    skew = [0]

    for i in range(len(Genome)):
        if Genome[i] == 'C':
            skew.append(skew[i] - 1)
        elif Genome[i] == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
    return skew

def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    mini = min(skew)
    positions = []
    for num in range(len(skew)):
        if skew[num] == mini:
            positions.append(num)
    return positions

def HammingDistance(p, q):
    mismatch = 0
    pstring = p
    qstring = q

    for i in range(len(p)):
        if pstring[i] == qstring[i]:
            mismatch += 0
        else:
            mismatch += 1
    return mismatch

def ApproximatePatternMatching(Genome,pattern,d):
    positions = []
    for i in range(len(Genome) - len(pattern) + 1):
        if HammingDistance(Genome[i : i + len(pattern)],pattern):
            positions.append(i)
    return positions

def ApproximatePatternCount(Genome,pattern,d):
    count = 0
    for i in range(len(Genome) - len(pattern) + 1):
        if HammingDistance(Genome[i : i + len(pattern)],pattern) <= d:
            count += 1
    return count



print(FrequentWords("ATGCATCG",2))
