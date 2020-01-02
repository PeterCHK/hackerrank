def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output

nums=[1,2,3,4,5]
