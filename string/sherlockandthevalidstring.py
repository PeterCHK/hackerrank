from collections import Counter
def isValid(s):
    b = min(Counter(s).values())
    a = Counter(dict.fromkeys(s,b))
    if sum(Counter(s).values())-sum(a.values()) > 1:
        return 'NO'
    return 'YES'

s1 = 'AAB'
s2 = 'AABB'
s3 = 'abcdefghhgfedecba'
print(isValid(s3))
