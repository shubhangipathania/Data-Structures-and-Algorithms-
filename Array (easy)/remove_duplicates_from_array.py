#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
#Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
#The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
def remove_duplicates(nums):
    n = len(nums)
    if (n==1):
        return 1
    i = 0
    j = i+1
    while (j < n):
        if (nums[j] != nums[i]):
            i += 1
            nums[i],nums[j] = nums[j], nums[i]

        j += 1
    return i+1, nums 


nums=[1,1,2,3,3,4,5,6,7,7,8,10]
output= remove_duplicates(nums)
print(output)