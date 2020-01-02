def minimumAbsoluteDifference(arr):
    arr.sort()
    diff=0
    mindiff=abs(arr[-1]-arr[-2])
    for i in range(len(arr)-1,0,-1):
        diff=abs(arr[i]-arr[i-1])
        if diff<mindiff:
            mindiff=diff
    return mindiff

arr=[1,3,5,4]
print(minimumAbsoluteDifference(arr))
