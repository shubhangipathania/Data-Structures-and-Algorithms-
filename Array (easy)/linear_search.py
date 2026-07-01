#Given an array, arr[] of n integers, and an integer element x, 
# find whether element x is present in the array.
# Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.
def linear_search(arr,target):
    n = len(arr)
    for i in range(0,n):
        if(arr[i] == target):
            return i 
    return -1


arr=[4,6,7,8,3,2,3,4,5,6,7,8,0]
arr2=[4,2,3,11,34,8,6,45,33]
output1 = linear_search(arr,8)
output2 = linear_search(arr,100)
print(output1)
print(output2)