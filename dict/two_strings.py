def twoStrings(s1, s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            return 'YES'
    return 'NO'

for i in s1:
    print(i)
#print(twoStrings('hello','world'))
