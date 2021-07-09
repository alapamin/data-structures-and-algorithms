def sortedSquares(self, nums): #square all elements in a list and then sort them in O(nlog(n)) time using timSort
    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
    nums.sort()
    return nums
        