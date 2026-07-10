#Given an integer array nums, return all the triplets [nums[i], 
#nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.
def three_sum(nums):
    ans = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        if (i != 0) and (nums[i] == nums[i-1]):
            continue

        j = i+1
        k = n-1
        while (j < k):
            total_sum = nums[i] + nums[j] + nums[k]
            if(total_sum < 0):
                j += 1
            elif(total_sum > 0):
                k -= 1
            else:
                temp =[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j += 1
                k -= 1 
                while (j < k) and (nums[j] == nums[j-1]):
                    j += 1

                while (j < k) and (nums[k] == nums[k+1]):
                    k -= 1

    return ans


nums = [-1,0,-1,1,2,-4]
output = three_sum(nums)
print(output)
                
        