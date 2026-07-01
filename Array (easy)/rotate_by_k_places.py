#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
def rotate(arr,k):
    n = len(arr)
    k = k % n

    def reverse(left,right):
        while left < right :
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
        return arr
    
    reverse(n-k,n-1)
    reverse(0,n-k-1)
    a=reverse(0,n-1)
    print(a)


arr=[5,8,7,3,1,2,4,5,8,9,5,6,34]
output = rotate(arr,5)
