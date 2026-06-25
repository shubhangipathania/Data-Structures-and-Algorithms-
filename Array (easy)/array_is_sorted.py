#check if the array is sorted or not
def array_is_sorted(arr):
    n = len(arr)
    for i in range(0,n):
        if(arr[i] > arr[i+1]):
            return False
    return True
arr = [34,65,23,67,89,98,54]
output= array_is_sorted(arr)
print(output)