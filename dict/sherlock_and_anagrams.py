a = 'ifailuhkqq'
b = 'kkkk'

#my ans
def anagram(lst):
    count=0
    for i,x in enumerate(lst):
        for j,y in enumerate(lst[min(i+1,len(lst)):]):
            j_length = len(lst[min(i+1,len(lst)):])
            for k in range(len(lst)-1):
                if i+k > len(lst) or j+k > len(lst):
                    continue
                else:
                    if lst[i:i+k] == lst[len(lst)-j_length:len(lst)-j_length+k]:
                        count +=1
                        print(i,j,k,lst[i:i+k])
    return count

print(anagram(a))
"""
#community answer
from collections import Counter
from itertools import combinations

def sherlockAndAnagrams(s):
count = []
for i in range(1,len(s)+1):
    a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
    b = Counter(a)
    count.append(sum([len(list(combinations(['a']*b[j],2))) for j     in b]))
return sum(count)
"""
