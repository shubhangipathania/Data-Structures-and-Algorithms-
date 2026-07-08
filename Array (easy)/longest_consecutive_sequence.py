#Given an unsorted array of integers nums, 
#return the length of the longest consecutive elements sequence.
#Better 
def longest_consecutive_sequence(nums):
    n = len(nums)
    last_smaller = float("-inf")
    count = 0
    longest = 0
    i = 0
    while(i < n):
        if((nums[i] - last_smaller) > 1 ):
            count = 1
            last_smaller = nums[i]
            i += 1

        if((nums[i] - last_smaller) == 0):
            i += 1
        
        if((nums[i] - last_smaller ) == 1):
            count += 1
            last_smaller = nums[i]
            i += 1
        longest = max(longest,count)

    return longest

nums = [1,1,1,2,3,4,5,98,99,100,101,102,103,104]
output = longest_consecutive_sequence(nums)
print(output)


#optimal
def longest_consective(arr):
    n_len = len(arr)
    my_set = set()
    for i in range(0,n_len):
        my_set.add(arr[i])
        

    longest2 = 0
    count2 = 0
    for num in my_set:
        if (num - 1) not in my_set:
            x = num
            count2 = 1
            while (x+1) in my_set:
                count2 += 1
                x += 1

            longest2 = max(longest2,count2)

    return longest2
 


arr = [1,99,101,98,2,5,3,100,1,1]
output2 = longest_consective(arr)
print(output2)

