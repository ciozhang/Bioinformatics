def PatternCount(Text, Pattern):
	count=0
	for i in range(len(Text)-len(Pattern)+1):
		if Text[i:i+len(Pattern)]==Pattern:
			count+=1
	return count

def FrequentWords(Text,k):
    FrequentPatterns = []
    Count = {}
    k = int(k)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Text,Pattern)
    maxCount = max(Count.values())
    for i in Count:
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:i+k])
    return list(set(FrequentPatterns))

def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    for i in Pattern:
        if i == 'A':
            revComp += 'T'
        elif i == 'T':
            revComp += 'A'
        elif i == 'C':
            revComp += 'G'
        elif i == 'G':
            revComp += 'C'
        else:
        	print('not ATCG, somrthing wrong')
    return revComp[::-1]

def PatternMatching(Pattern, Genome):
	positions=[]
	for i in range(len(Genome)-len(Pattern)+1):
		if Pattern == Genome[i:i+len(Pattern)]:
			positions.append(i)
	return positions

def ClumpFinding_0(Genome,k,L,t):
	kmers = []
	k = int(k)
	L = int(L)
	t = int(t)
	for i in range(len(Genome)-L+1):
		Fragment = Genome[i:i+L]
		for j in range(L-k+1):
			Pattern = Fragment[j:j+k]
			if PatternCount(Fragment,Pattern) >= t:
				kmers.append(Pattern)
	return list(set(kmers))

def SymbolToNumber(Symbol):
    if 'A' in Symbol:
        return 0
    elif 'C' in Symbol:
        return 1
    elif 'G' in Symbol:
        return 2
    elif 'T' in Symbol:
        return 3

def PatternToNumber(Pattern):
    if len(Pattern)==1:
        return SymbolToNumber(Pattern)
    else:
        symbol = Pattern[-1]
        Prefix = Pattern[:-1]
        return 4 * PatternToNumber(Prefix) + SymbolToNumber(symbol)

def NumberToSymbol(index):
    index = int(index)
    if index == 0:
        return 'A'
    elif index == 1:
        return 'C'
    elif index == 2:
        return 'G'
    elif index == 3:
        return 'T'

def NumberToPattern(index, k):
    index = int(index)
    k = int(k)
    if k == 1:
        return NumberToSymbol(index)
    else:
        prefixIndex = index//4
        r = index%4
        symbol = NumberToSymbol(r)
        return NumberToPattern(prefixIndex,k-1)+symbol

def ComputingFrequencies(Text, k):
    k = int(k)
    FrequencyArray = [0 for _ in range(4**k)]
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        index = PatternToNumber(Pattern)
        FrequencyArray[index] += 1
    return FrequencyArray

def FasterFrequentWords(Text, k):
    k = int(k)
    FrequentPatterns = []
    FrequencyArray = ComputingFrequencies(Text, k)
    maxCount = max(FrequencyArray)
    for i in range(4**k):
        if FrequencyArray[i] == maxCount:
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def FindingFrequentWordsBySorting(Text , k):
    k = int(k)
    FrequentPatterns = []
    Index = {}
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index.values())
    for i in range(1, len(Text)-k+1):
        if SortedIndex[i] == SortedIndex[i-1]:
            Count[i] = Count[i-1]+1
    maxCount = max(Count.values())
    for i in range(len(Text)-k+1):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def ClumpFinding(Genome, k, t, L):
    FrequentPatterns = []
    Clump = [0 for _ in range(4**k)]
    for i in range(len(Genome)-L+1):
        Text = Genome[i:i+L]
        FrequencyArray = ComputingFrequencies(Text, k)
        for index in range(4**k):
            if FrequencyArray[index] >= t:
                Clump[index] = 1
    for i in range(4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def BetterClumpFinding(Genome,k,t,L):
    k = int(k)
    t = int(t)
    L = int(L)
    FrequentPatterns = []
    Clump = [0 for _ in range(4**k)]
    Text = Genome[0:L]
    FrequencyArray = ComputingFrequencies(Text,k)
    for i in range(4**k):
        if FrequencyArray[i] >= t:
            Clump[i] = 1
    for i in range(1, len(Genome)-L+1):
        FirstPattern = Genome[i-1:i-1+k]
        index = PatternToNumber(FirstPattern)
        FrequencyArray[index] -= 1
        LastPattern = Genome[i+L-k:i+L]
        index = PatternToNumber(LastPattern)
        FrequencyArray[index] += 1
        if FrequencyArray[index] >= t:
            Clump[index] = 1
    for i in range(4**k):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i,k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

