import sys

a = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    a.append(arr_temp)

max_sum =-63

for i in range(4):
    for j in range(4):
        check_sum = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]

        if check_sum > max_sum:
            max_sum = check_sum

print (max_sum)
