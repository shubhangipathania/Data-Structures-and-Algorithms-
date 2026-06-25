#Right rotate the array by one place.
nums= [34,67,89,54,23,45,76,89,11,43,22]
n= len(nums)
nums[:]= [nums[-1]]+ [nums[0:n-1]]
print(nums)

#Another way
arr=[45,76,89,32,12,56,45,22,78]
n= len(arr)
temp = arr[n-1]
for i in range(n-2,-1,-1):
    arr[i+1] = arr[i]
arr[0] = temp 
print(arr)