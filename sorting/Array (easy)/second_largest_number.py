#Second largest element in an array without sorting
def second_largest_number(arr):
    largest_number = float("-inf")
    s_largest_number = float("-inf")
    n = len(arr)
    for i in range(0,n):
        if(arr[i] > largest_number):
            s_largest_number = largest_number
            largest_number = arr[i]
        elif(arr[i] > s_largest_number) and (arr[i] != largest_number):
            s_largest_number = arr[i]

    return largest_number, s_largest_number

arr= [45,76,23,89,56,21,34,10]
output = second_largest_number(arr)
print(output)