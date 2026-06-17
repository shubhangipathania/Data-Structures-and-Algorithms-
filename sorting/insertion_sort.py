#Given an array arr[] of positive integers.The task is to complete the insertsort() function which is used to implement Insertion Sort.
def insertion_sort(arr):
    n= len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while (j>=0) and (arr[j]> key):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr


nums=[4,7,6,8,3,5,2,4,1,10]
output= insertion_sort(nums)
print(output)