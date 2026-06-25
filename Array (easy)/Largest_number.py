#Given an array arr[]. The task is to find the largest element and return it.
def largest_number(arr):
    largest = arr[0]
    n = len(arr)
    for i in range(0,n):
        largest = max(largest, arr[i])
    return largest

nums=[56,78,34,-87,37,23,99,65]
output= largest_number(nums)
print(output)