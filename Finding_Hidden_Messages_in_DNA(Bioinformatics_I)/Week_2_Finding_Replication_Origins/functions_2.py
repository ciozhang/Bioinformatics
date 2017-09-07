import sys
sys.path.extend(['Week_1_Welcome'])   # run in path 'Bioinformatics\Finding_Hidden_Messages_in_DNA(Bioinformatics_I)'
from functions_1 import *

def MinimumSkew(Genome):
    Skew = [0 for _ in range(len(Genome)+1)]
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == 'G':
            Skew[i] = Skew[i-1]+1
        elif Genome[i-1] == 'C':
            Skew[i] = Skew[i-1]-1
        else:
            Skew[i] = Skew[i-1]
    minSkew = min(Skew)
    output = []
    for i in range(len(Skew)):
        if Skew[i] == minSkew:
            output.append(i)
    return output

def HammingDistance(p, q):
    assert len(p) == len(q)
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count+=1
    return count

def ApproximatePatternMatching(Pattern, Text, d):
    d = int(d)
    positions=[]
    k = len(Pattern)
    for i in range(len(Text)-k+1):
        if HammingDistance(Pattern,Text[i:i+k]) <= d:
            positions.append(i)
    return positions

def ApproximatePatternCount(Pattern, Text, d):
    d = int(d)
    count = 0
    k = len(Pattern)
    for i in range(len(Text)-k+1):
        if HammingDistance(Pattern,Text[i:i+k]) <= d:
            count+=1
    return count

def Neighbors(Pattern, d):
    d = int(d)
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A','C','G','T']
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:],Text) < d:
            for x in ['A','C','G','T']:
                Neighborhood.append(x+Text)
        else:
            Neighborhood.append(Pattern[0]+Text)
    return Neighborhood

def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequenciesArray = [0 for i in range(4**k)]
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Neighborhood = Neighbors(Pattern, d)
        for s in Neighborhood:
            j = PatternToNumber(s)
            FrequenciesArray[j] += 1
    return FrequenciesArray

def ComputingWordsWithMismatches(Text, k, d):
    k = int(k)
    d = int(d)
    FrequentPatterns = []
    Neighborhoods = []
    for i in range(len(Text)-k+1):
        if d == 0:
            Neighborhoods.append(Text[i:i+k])
        else:
            for j in Neighbors(Text[i:i+k],d):
                Neighborhoods.append(j)
    Index = [0 for i in range(len(Neighborhoods))]
    Count = [0 for i in range(len(Neighborhoods))]
    for i in range(len(Neighborhoods)):
        Pattern = Neighborhoods[i]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index)
    for i in range(len(Neighborhoods)-1):
        if SortedIndex[i] == SortedIndex[i+1]:
            Count[i+1] = Count[i]+1
    maxCount = max(Count)
    for i in range(len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def ComputingWordsWithMismatchesandReverseComplement(Text, k, d):
    k = int(k)
    d = int(d)
    FrequentPatterns = []
    Neighborhoods = []
    for i in range(len(Text)-k+1):
        if d == 0:
            Neighborhoods.append(Text[i:i+k])
            Neighborhoods.append(ReverseComplement(Text)[i:i+k])
        else:
            for j in Neighbors(Text[i:i+k],d):
                Neighborhoods.append(j)
            for j in Neighbors(ReverseComplement(Text)[i:i+k],d):
                Neighborhoods.append(j)
    Index = [0 for i in range(len(Neighborhoods))]
    Count = [0 for i in range(len(Neighborhoods))]
    for i in range(len(Neighborhoods)):
        Pattern = Neighborhoods[i]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index)
    for i in range(len(Neighborhoods)-1):
        if SortedIndex[i] == SortedIndex[i+1]:
            Count[i+1] = Count[i]+1
    maxCount = max(Count)
    for i in range(len(Neighborhoods)):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns