import random
import sys
sys.path.extend(['Week_3_Hunting_for_Regulatory_Motifs'])   # run in path 'Bioinformatics\Finding_Hidden_Messages_in_DNA(Bioinformatics_I)'
from functions_3 import *

def RandomizedMotifSearch(Dna, k, t):
    k = int(k)
    t = int(t)
    Motifs = []
    for Text in Dna:
        i = random.randrange(len(Text)-k+1)
        Motifs.append(Text[i:i+k])
    BestMotifs = Motifs
    while True:
        profile = Profile(Motifs)
        Motifs = motifs(profile, k, Dna)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        else:
            return BestMotifs

def motifs(profile, k, Dna):
    Motifs = []
    for Text in Dna:
        Motifs.append(ProfileMostProbableKmer(Text, k, profile))
    return Motifs

def ProfileRandomly(Text, k, Matrix):
    probabilityDistribution = []
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
        probabilityDistribution.append(profile)
    wheel = [0]*(len(probabilityDistribution)+1)
    s = sum(probabilityDistribution)
    """normalization in case where probabilityDistribution is not normalized """
    if s!=1:
        probabilityDistribution = [(1.*x)/s for x in probabilityDistribution]
    """creating the roulette wheel """
    for i, prob in enumerate(probabilityDistribution):
        wheel[i+1] = wheel[i] + prob
    """spinning the wheel """ 
    r = random.random()
    result = 0
    for i in range(len(wheel)-1):
        if r>wheel[i] and r<wheel[i+1]:
            result = Text[i:i+k]
    return result

def GibbsSample(Dna, k, t, N):
    k = int(k)
    t = int(t)
    N = int(N)
    Motifs = []
    for Text in Dna:
        i = random.randrange(len(Text)-k+1)
        Motifs.append(Text[i:i+k])
    for _ in range(N):
        i = random.randrange(t)
        temp = Motifs[:i]+Motifs[i+1:]
        profile = Profile(temp)
        Motifs[i] = ProfileRandomly(Dna[i], k, profile)
    BestScore = float('inf')
    if Score(Motifs) < BestScore:
        BestMotifs = Motifs
        BestScore = Score(Motifs)
    return BestMotifs