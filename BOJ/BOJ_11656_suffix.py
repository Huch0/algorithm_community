S = input()

suffixList = [S[x:] for x in range(len(S))]

for k in sorted(suffixList):
    print(k)