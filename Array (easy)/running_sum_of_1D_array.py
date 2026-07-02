#Given an array nums.
#  We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.
def running_sum(nums):
    n = len(nums)
    r_sum = [0] * n 
    r_sum[0] = nums[0]
    for i in range(1,n):
       r_sum[i] = r_sum[i-1] + nums[i]
    return r_sum

nums= [1]
output = running_sum(nums)
print(output)

 