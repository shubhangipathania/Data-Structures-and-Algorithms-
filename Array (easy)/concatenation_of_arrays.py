#Given an integer array nums of length n,
#you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums arrays.
#Return the array ans.
def concatenation_of_arrays(nums):
    n = len(nums)
    ans = [0] * (2*n)
    for i in range(0,n):
        ans[i] = nums[i]
        ans[i+n] = nums[i]
    return ans

nums =[1,2,3,4,5]
output = concatenation_of_arrays(nums)
print(output)