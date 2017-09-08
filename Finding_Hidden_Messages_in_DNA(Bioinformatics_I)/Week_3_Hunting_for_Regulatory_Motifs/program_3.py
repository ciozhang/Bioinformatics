# run in path 'Bioinformatics\Finding_Hidden_Messages_in_DNA(Bioinformatics_I)'
from functions_3 import *

import sys
lines = sys.stdin.read().splitlines()
Dna = []
#for i in lines[1].split(' '):
#	Dna.append(i)

for i in lines[1:]:
	Dna.append(i)

#k,d = lines[0].split(' ')
#print(' '.join(str(i) for i in MotifEnumeration(Dna, k, d)))

#print(DistanceBetweenPatternAndStrings(lines[0], Dna))

print(MedianString(Dna,lines[0]))