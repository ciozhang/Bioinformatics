import sys
sys.path.extend(['Week_2_Finding_Replication_Origins'])   # run in path 'Bioinformatics\Finding_Hidden_Messages_in_DNA(Bioinformatics_I)'
from functions_2 import *

def MotifEnumeration(Dna, k, d):
    k = int(k)
    d = int(d)
    Neighborhoods = [[] for i in range(len(Dna))]
    for i in range(len(Dna)):
        Text = Dna[i]
        for j in range(len(Text)-k+1):
            if d == 0:
                Neighborhoods[i].append(Text[j:j+k])
            else:
                for z in Neighbors(Text[j:j+k],d):
                    Neighborhoods[i].append(z)
    result = set(Neighborhoods[0])
    for s in Neighborhoods[1:]:
        result.intersection_update(s)
    return list(result)

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        hammingDistance = float("inf")
        for i in range(len(Text)-k+1):
            if hammingDistance > HammingDistance(Pattern, Text[i:i+k]):
                hammingDistance = HammingDistance(Pattern, Text[i:i+k])
        distance += hammingDistance
    return distance

def MedianString(Dna,k):
    k = int(k)
    distance = float('inf')
    for i in range(4**k):
        Pattern = NumberToPattern(i,k)
        if distance > DistanceBetweenPatternAndStrings(Pattern,Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern,Dna)
            Median = Pattern
    return Median