from functions import *

import sys
lines = sys.stdin.read().splitlines()

#print(' '.join(str(i) for i in MinimumSkew(lines[0])))

#print(HammingDistance(lines[0],lines[1]))

#print(' '.join(str(i) for i in ApproximatePatternMatching(lines[0],lines[1],lines[2])))

#print(ApproximatePatternCount(lines[0],lines[1],lines[2]))

print('\n'.join(str(i)for i in Neighbors(lines[0],lines[1])))