#Well, I created a temporary array (temp) to store the position (pos) of elements (val) in the original array (since they are consecutive). Then I referred to the positions in order to bring the original array into order: I looked for 1, and wherever that 1 is, I placed the element at index 0 of arr and then updated its new position in temp as well; looked for 2, wherever that 2 is, I placed the element at index 1 of arr and then updated its new position in temp... If any element is at its right place, I skipped else increased the swaps.



def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    print(temp)
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps



def minimumSwaps2(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        #pos += 1
    print(temp)
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps



arr = [2,3,5,4,1]
def minimumSwaps3(arr):
    for i in arr:
        if i != arr.index(i)+1:
            print(i,arr.index(i)+1,arr.index(i),arr.index(i)+1)
            tmp1 = arr.index(i)
            tmp2 = arr.index(i)+1
            arr[tmp1],arr[tmp2] = arr[tmp2],arr[tmp1]
            #arr[arr.index(i)],arr[arr.index(i)+1] = arr[arr.index(i)+1],arr[arr.index(i)]
            print(arr)
            print(i,arr.index(i)+1,arr[arr.index(i)],arr[arr.index(i)+1])
    return arr

def minimumSwaps4(arr):
    print(arr)
    arr[0],arr[1] = arr[1],arr[0]
    print(arr)

def minimumSwaps5(arr):
    NumList = arr
    Number = len(arr)
    count = 0
    for i in range (Number):
        for j in range(i + 1, Number):
            if(NumList[i] > NumList[j]):
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp
                count +=1
    return count

print(minimumSwaps2(arr))
