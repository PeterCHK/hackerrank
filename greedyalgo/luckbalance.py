from itertools import compress
L=[5,2,1,8,10,5]
T=[1,1,1,1,0,0]
k=3

def luckBalance(k, contests):
    _sum=0
    a = sorted(list(compress(list(zip(*contests))[0],list(zip(*contests))[1])),reverse=True)
    for i in range(k):
        _sum += a[i]
    for i in range(k,len(a)):
        _sum -= a[i]
    for i,v in sorted(contests, key=lambda item:item[1]):
        if v == 0:
            _sum+=i
    return _sum

print(luckBalance(k,list(zip(L,T))))
