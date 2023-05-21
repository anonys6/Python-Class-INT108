S = "aeroplane"

v = "aeiouAEIOU"

conS = ""
vowS = ""

for i in S:
    if i in v:
        vowS = vowS + i
    else:
        conS = conS + i


''.join(sorted(conS))
''.join(sorted(vowS))


word = ""

k = 0

for i in conS, vowS:
    if k % 2 == 0:
        word = word+ i
    else:
        word = word + cow
    k = k + 1