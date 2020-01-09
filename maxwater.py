
# Python3 code for the above approach

# Return the maximum water
# that can be stored
def maxWater(height, n) :
    maximum = 0;

    # Check all possible pairs of buildings
    for i in range(n - 1) :
        for j in range(i + 1, n) :
            current = min(height[i],
                          height[j]) * (j - i - 1);

            # Maximum so far
            maximum = max(maximum, current);

    return maximum;

# Driver code
if __name__ == "__main__" :
    height = [ 2, 1, 3, 4, 6, 5 ];

    n = len(height);
    print(maxWater(height, n));

# This code is contributed by AnkitRai01
