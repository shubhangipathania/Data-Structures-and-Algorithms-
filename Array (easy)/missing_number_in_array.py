#Given an array nums containing n distinct numbers in the range [0, n] 
#return the only number in the range that is missing from the array.
#BruteForce
nums= [ 3,4,5,6,7,0,1,8]
n = len(nums)
for i in range(0, n+1):
    if i not in nums:
        print(i) 

#Better 
arr=[3,2,9,10,0,1,4,5,6,7]
nlen = len(arr)
freq = {}
for i in range(0,n+1):
    freq[i] = 0
for num in arr:
    freq[num] = 1 
for k,v in freq.items():
    if (v==0):
        print(k)

#optimal
nums2 = [4,5,2,0,7,8,9,10,1,3]
nno = len(nums2)
sum_of_n_numbers = nno *(nno +1)//2
sum = 0
for j in range(0,nno):
    sum = sum + nums2[j]
print(sum_of_n_numbers - sum)