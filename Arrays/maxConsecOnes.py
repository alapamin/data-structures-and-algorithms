
def findMaxConsecutiveOnes(nums):
    counter = 0
    greatest = 0
    for i in nums: #iterate through list 
        if i == 1: #if it's one then we add to counter
            counter+=1
            if counter > greatest:
                greatest = counter #since we added to counter, lets check to see if it's greater than the highest count
        else:
            counter = 0 #otherwise we just set counter to 0 b/c it's not consecutive
    return greatest

potato = [1,0,0,0,1,1,1,1,0,1,1,1,1]

print(findMaxConsecutiveOnes(potato))