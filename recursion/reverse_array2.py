#Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).
def funcArray(arr,l,r):
	    # code here
	if ( l>=r ):
		return 
		
	arr[l],arr[r] = arr[r],arr[l]
	funcArray(arr, l+1, r-1)
		
		
def reverseSubArray(arr,l,r):
	# l -= 1
	# r -= 1
	funcArray(arr,l,r)
	return arr

arr=[3,6,5,3,3,4,6,7,8,1,2,3,7]
a=reverseSubArray(arr,4,12)
print(a)