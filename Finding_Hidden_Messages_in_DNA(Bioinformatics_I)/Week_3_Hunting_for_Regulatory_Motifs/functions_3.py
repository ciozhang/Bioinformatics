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

def ProfileMostProbableKmer(Text, k, Matrix):
    k = int(k)
    Profile = -float('inf')
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        profile = 1
        for j in range(k):
            if Pattern[j] == 'A':
                profile *= float(Matrix[0][j])
            elif Pattern[j] == 'C':
                profile *= float(Matrix[1][j])
            elif Pattern[j] == 'G':
                profile *= float(Matrix[2][j])
            elif Pattern[j] == 'T':
                profile *= float(Matrix[3][j])
            else:
                print("not'ACGT', something wrong")
        if Profile < profile:
            Profile = profile
            kmer = Pattern
    return kmer

def Profile(motifs):
    Matrix = [[1. for i in range(len(motifs[0]))] for i in range(4)]
    for i in range(len(motifs)):
        for j in range(len(motifs[i])):
            if len(motifs[0]) == 1:
                last = i
            else:
                last = j
            if motifs[i][j] == 'A':
                Matrix[0][last] += 1
            elif motifs[i][j] == 'C':
                Matrix[1][last] += 1
            elif motifs[i][j] == 'G':
                Matrix[2][last] += 1
            elif motifs[i][j] == 'T':
                Matrix[3][last] += 1
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            Matrix[i][j] /= (len(motifs)+4)
    return Matrix

def Score(motifs):
    Matrix = Profile(motifs)
    score = (len(motifs)+1)*len(motifs[0])
    for i in range(len(Matrix[0])):
        score -= max(Matrix[j][i] for j in range(len(Matrix)))*(len(motifs)+4)
    return score

def GreedyMotifSearch(Dna,k,t):
    k = int(k)
    t = int(t)
    assert t == len(Dna)
    bestMotifs = [Dna[i][:k] for i in range(t)]
    for i in range(len(Dna[0])-k+1):
        motifs = [Dna[0][i:i+k]]
        for j in range(1,t):
            motifs.append(ProfileMostProbableKmer(Dna[j],k,Profile(motifs)))
        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs