a={}
m = 'give me one grand today night'
n = 'give one grand today'
m2 = m.split()
for i in range(len(m2)):
    a[m2[i]]=1

for i in n.split():
    if a.get(i,0) == 0:
        return False
    
return True
