#Given an array arr, use selection sort to sort arr[] in increasing order.
def selection_sort(arr):
    n= len(arr)
    for i in range(0,n):
        min_index = i 
        for j in range(i+1,n):
            if(arr[j]< arr[min_index]):
                min_index = j 

        arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr


output= selection_sort([3,6,7,5,3,2,3,2,9])
print(output)