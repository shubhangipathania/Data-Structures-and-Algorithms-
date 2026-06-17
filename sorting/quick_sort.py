#Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
#Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().
def quick_sort(arr,low,high):
    if(low < high):
        p_index= partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr,p_index + 1, high)
        return arr
    

def partition(arr, low, high):
    pivot= arr[low]
    i=low
    j= high
    while(i<j):
        while (i<= high-1) and (arr[i] <= pivot):
            i += 1
        while (j>= low+1) and (arr[j] > pivot):
            j -= 1
        if(i<j):
            arr[i],arr[j] = arr[j], arr[i]
    arr[low], arr[j]= arr[j], arr[low]
    return j 


arr=[4,6,7,8,3,2,1,6]
output= quick_sort(arr, 0 , len(arr)-1)
print(output)