def maximumToys(prices, k):
    prices.sort()
    print(prices)
    count = 0
    for i in prices:
        k = k - i
        if k > 0:
            count +=1
    return count

prices=[2,5,7,9,4,2]
k=10
print(maximumToys(prices,k))
