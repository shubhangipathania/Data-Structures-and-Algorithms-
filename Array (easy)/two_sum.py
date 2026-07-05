#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.
#You can return the answer in any order.
def two_sum(nums,target):
    n = len(nums)
    hash_map = {}
    for i in range(0,n):
        remaining_element = target - nums[i]
        if (remaining_element in hash_map):
            return [hash_map[remaining_element],i]
        
        hash_map[nums[i]] = i



nums= [5,9,1,2,4,15,6,3]
output = two_sum(nums,13)
print(output)