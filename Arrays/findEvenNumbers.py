def findNumbers(self, nums): #This function returns the amount of integers that have an even amount of digits within them from a list.
    counter = 0
    for i in nums:
        if (len(str(i)))%2==0:
            counter+=1
    return counter