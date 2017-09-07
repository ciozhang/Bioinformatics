from functions import *

#import sys
#lines = sys.stdin.read().splitlines()

#print(HammingDistance(lines[0],lines[1]))

#print(' '.join(str(i) for i in ApproximatePatternMatching(lines[0],lines[1],lines[2])))

#print(ApproximatePatternCount(lines[0],lines[1],lines[2]))

#print('\n'.join(str(i)for i in Neighbors(lines[0],lines[1])))

#print(ComputingFrequenciesWithMismatches('AAGCAAAGGTGGG', 2, 1))

#k,d = lines[1].split(' ')
#print(' '.join(str(i) for i in ComputingWordsWithMismatches(lines[0],k,d)))

#k,d = lines[1].split(' ')
#print(' '.join(str(i) for i in ComputingWordsWithMismatchesandReverseComplement(lines[0],k,d)))

#string = ''
#for i in range(1,len(lines)):
#	string += lines[i]
#print(' '.join(str(i) for i in MinimumSkew(string)))
#print(string[3764800:3764900])

print(len(Neighbors('TGCAT',2)))