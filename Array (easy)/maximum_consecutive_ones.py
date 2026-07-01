#Given a binary array nums, return the maximum number of consecutive 1's in the array.
def maximum_consecutive_ones(nums):
    count = 0
    max_count = 0
    for i in range(0,len(nums)):
        if(nums[i] == 1):
            count += 1
        else:
            max_count = max(count,max_count)
            count = 0
    return max(count,max_count)


nums=[1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1]
output = maximum_consecutive_ones(nums)
print(output)