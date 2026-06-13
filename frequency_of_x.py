#You're given an array (arr)
#Return the frequency of element x in the given array
def findfrequency(arr,x):
    count = 0
    for i in range(0, len(arr)):
        if(arr[i] == x):
            count += 1
    print(count)


findfrequency([1,2,3,4,5,5,3,2], 5)