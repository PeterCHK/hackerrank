import re
def substrCount(n, s):
    count = len(s)

    exp1 = r'(([a-z])\2*)(?!\1)(?=[a-z]\1)'
    m = re.finditer(exp1,s)
    #count += sum([len(x.group(0)) for x in m])
    print(([len(x.group(0)) for x in m])

    exp2 = r'([a-z])\1+'
    m = re.finditer(exp2,s)
    count += sum([triangular_number(len(x.group(0))-1) for x in m])

    return count

def triangular_number(n):
      return (pow(n,2)+n)//2


s1 = 'asasd'
s2 = 'abcbaba'
s3 = 'aaaa'

print(substrCount(len(s1),s1))
#print(substrCount(len(s2),s2))
#print(substrCount(len(s3),s3))
