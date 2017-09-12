from functions_4 import *
'''
import sys
lines = sys.stdin.read().splitlines()
Dna = []
for i in lines[1:]:
    Dna.append(i)
k,t = lines[0].split(' ')
'''
'''
BestScore = float('inf')
for _ in range(1000):
    Motifs = RandomizedMotifSearch(Dna, k, t)
    if Score(Motifs) < BestScore:
        BestMotifs = Motifs
        BestScore = Score(Motifs)
print('\n'.join(str(i) for i in BestMotifs))
'''

Dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']


BestScore = float('inf')
for _ in range(20):
    Motifs = GibbsSample(Dna,8,5,100)
    if Score(Motifs) < BestScore:
        BestMotifs = Motifs
        BestScore = Score(Motifs)
print('\n'.join(str(i) for i in BestMotifs))
print(Score(BestMotifs))