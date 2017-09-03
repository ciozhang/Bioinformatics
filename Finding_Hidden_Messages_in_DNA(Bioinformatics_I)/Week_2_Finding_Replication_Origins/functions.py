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

