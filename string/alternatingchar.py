def alternatingCharacters(s):
    s=str(s)
    new = ''
    new += s[0]
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            new += s[i]
    return len(s)-len(new)

s1='AAABBB'
s2='AAAA'
s3='BBBBB'
s4='ABABABAB'
s5='BABABA'
s6='AAABBB'
print(alternatingCharacters(s3))
