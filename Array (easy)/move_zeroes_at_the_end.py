#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Note that you must do this in-place without making a copy of the array.
def move_zeroes(nums):
    if (len(nums) == 1):
        return 
    i = 0
    while (i < len(nums)):
        if(nums[i] == 0):
            break
        i += 1
    if (i == len(nums)):
        return 
    j = i+1
    while (j < len(nums)):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j],nums[i]
            i += 1
        j += 1
    return nums

nums= [2,5,6,0,6,0,7,4,6,0,0,0,2]
output = move_zeroes(nums)
print(output)