def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = (letter == chr(i) for letter in a)
        ib = (letter == chr(i) for letter in b)
        count += abs(sum(ia)-sum(ib))
    return count

a = 'abc'
b = 'ced'
print(makeAnagram(a,b))
