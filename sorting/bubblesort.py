def countSwaps(a):
    _sorted = True
    count = 0
    while _sorted:
        _sorted = True
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                count +=1
            else:
                _sorted=False
    #print(count,a[0],a[])
    return 'Array is sorted in {} swaps. \nFirst Element: {} \nLast Element: {}'.format(count, a[0],a[len(a)-1])

a = [1,2,3]
b=[3,2,1]
c=[4,2,3,1]
print(countSwaps(a))
print(countSwaps(b))
print(countSwaps(c))
