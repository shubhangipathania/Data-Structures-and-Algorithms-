def reverseSubArray(arr,l,r):
    if(l>=r):
        print(arr)
        return     
    arr[l],arr[r]=arr[r],arr[l]
    reverseSubArray(arr,l+1,r-1)

list=[1,2,3,4,5,6]
reverseSubArray(list,0,5)
