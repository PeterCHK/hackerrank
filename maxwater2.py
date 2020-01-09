def maxWater(height,n):
    a = []
    for i in range(n):
        a.append([height[i],range(n)[i]])
    b = sorted(a, key=lambda x : x[0])

    minIndSoFar = b[n-1][1]
    maxIndSoFar = b[n-1][1]
    _max = 0
    for i in range(n-2,0,-1):
        #Current building paired with the building
        #greater in height and on the extreme left
        left = 0
        if minIndSoFar < b[i][1]:
            left = b[i][0] * (b[i][1] - minIndSoFar - 1)
        #Current building paired with the building
        #greater in height and on the extreme right
        right = 0
        if maxIndSoFar > b[i][1]:
            right = b[i][0] * (maxIndSoFar - b[i][1] - 1)
        #Maximum so far
        _max = max(left, right, _max)

        # Update the maximum and minimum so far
        minIndSoFar = min(minIndSoFar,b[i][1])
        maxIndSoFar = max(maxIndSoFar,b[i][1])

    return _max



if __name__ == "__main__" :
    height = [ 2, 1, 3, 4, 6, 5 ];

    n = len(height);
    print(maxWater(height, n));
