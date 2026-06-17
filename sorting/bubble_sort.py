#Given an array, arr[]. Sort the array using bubble sort algorithm.
def bubble_sort(arr):
    n= len(arr)
    for i in range(n-2, -1 , -1):
        is_swap= False
        for j in range(0, i+1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swap = True

        if(is_swap == False):
            return arr
        
    return arr

nums= [3,4,7,5,9,12,5,3]
output= bubble_sort(nums)
print(output)