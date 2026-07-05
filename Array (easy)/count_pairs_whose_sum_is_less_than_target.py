#Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
#Brute force
def count_pairs(nums,target):
    n= len(nums)
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if(nums[i] + nums[j] < target):
                count += 1
    return count


nums = [-1,1,2,3,1]
output = count_pairs(nums,2)
print(output)

#optimal Solution (using sorting and two pointers)
def count_pairs_whose_sum_is_less_than_the_target(arr,target2):
    n_len = len(arr)
    left = 0
    right = n_len-1
    count = 0
    while (left < right):
        if (arr[left] + arr[right] < target2):
            count = count + (right - left)
            left += 1
        else:
            right -= 1
    return count

arr = [-1,1,1,2,3]
output2 = count_pairs_whose_sum_is_less_than_the_target(arr,2)
print(output2)