#Given an integer array nums, find the subarray with the largest sum and return its sum.
#Brute Force
def maximum_subarray(nums):
    n = len(nums) 
    i = 0 
    j = 0
    total = 0 
    maximum = float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            total = total + nums[j]
            if(total > maximum):
                maximum = total 
        total = 0 
    return maximum 


nums = [5,4,-1,7,8]
output = maximum_subarray(nums)
print(output)


#Optimal (kandane's Algorithm)
def maximum_subarray_sum(arr):
    n = len(arr)
    maximum = float("-inf")
    total = 0
    for i in range(0,n):
        total = total + nums[i]
        maximum = max(total,maximum)
        if (total < 0):
            total = 0 

    return maximum


arr = [5,4,-1,7,8]
output2 = maximum_subarray_sum(arr)
print(output2)
