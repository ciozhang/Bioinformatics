import time
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

from functions import *

#print(PatternCount(lines[0], lines[1]))

'''
time_1 = time.time()
print(' '.join(str(i) for i in FrequentWords(lines[0],lines[1])))
print('-------%s seconds----------' % (time.time() - time_1))
time_2 = time.time()
print(' '.join(str(i) for i in FasterFrequentWords(lines[0],lines[1])))                         # small k
print('-------%s seconds----------' % (time.time() - time_2))
time_3 = time.time()
print(' '.join(str(i) for i in FindingFrequentWordsBySorting(lines[0],lines[1])))               # big k
print('-------%s seconds----------' % (time.time() - time_3))
'''

#print(ReverseComplement(lines[0]))

#print(' '.join([str(i) for i in PatternMatching('CTTGATCAT',lines[0])]))

'''
Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
time_0 = time.time()
print(ClumpFinding_0(Genome,5,50,4))
print('-------%s seconds----------' % (time.time() - time_0))
time_1 = time.time()
print(ClumpFinding(Genome,5,4,50))
print('-------%s seconds----------' % (time.time() - time_1))
time_2 = time.time()
print(BetterClumpFinding(Genome,5,4,50))
print('-------%s seconds----------' % (time.time() - time_2))
'''

#print(PatternToNumber(lines[0]))

#print(NumberToPattern(lines[0],lines[1]))

#print(' '.join(str(i) for i in ComputingFrequencies(lines[0],lines[1])))

#k,L,t = lines[1].split(' ')
#print(' '.join([str(i) for i in BetterClumpFinding(lines[0],k,t,L)]))
#print(len(BetterClumpFinding(lines[0],9,3,500)))
