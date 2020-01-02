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

arr = [2,3,1,5,4]
minimumSwaps(arr)
