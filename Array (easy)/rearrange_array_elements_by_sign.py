#You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should return the array of nums such that the array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
def rearrange_array_elements_by_sign(nums):
    n_len = len(nums)
    result = [0] * n_len
    p = 0
    n = 1
    for i in range(0, n_len):
        if(nums[i] >= 0):
            result[p] = nums[i]
            p += 2
        else:
            result[n] = nums[i] 
            n += 2

    return result


nums= [3,10,-3,-1,-10,6]
output = rearrange_array_elements_by_sign(nums)
print(output)