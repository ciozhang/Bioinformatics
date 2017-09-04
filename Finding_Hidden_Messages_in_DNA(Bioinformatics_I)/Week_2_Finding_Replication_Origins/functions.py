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