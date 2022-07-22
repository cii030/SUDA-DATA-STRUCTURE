def rank(nums):
    res = []
    i = 0
    while i < len(nums):
        j = 0
        value = 0
        while j < len(nums):
            if nums[j] < nums[i] or (nums[j] == nums[i] and j < i):
                value += 1
            j += 1
        i += 1
        res.append(value)
    return res


n = input()
lst = list(map(int, n.split()))
print(rank(lst))
'''时间复杂度O(n2)'''
