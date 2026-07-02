#Given a zero-based permutation nums (0-indexed),
#build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
#A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
def build_array_from_permutation(nums):
    n = len(nums)
    arr=[]
    for i in range(0,n):
        arr.append(nums[nums[i]])
    return arr

nums = [4,7,8,3,2,1,0,5,6]
output = build_array_from_permutation(nums)
print(output)