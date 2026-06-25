#You have been given an array ‘a’ of ‘n’ unique non-negative integers.
#Find the second largest and second smallest element from the array.
#Return the two elements (second largest and second smallest) as another array of size 2.
def getSecondOrderElements(a):
    n= len(a)
    largest_element = float("-inf")
    second_largest_element = float("-inf")
    small_element = float("inf")
    second_small_element = float("inf")
    for i in range(0,n):
        if(a[i] > largest_element):
            second_largest_element = largest_element
            largest_element = a[i]
        if(a[i] > second_largest_element) and (a[i] != largest_element):
            second_largest_element = a[i]
        if(a[i] < small_element):
            second_small_element = small_element
            small_element = a[i]
        if(a[i] < second_small_element) and (a[i] != small_element):
            second_small_element = a[i]
    return [second_largest_element,second_small_element]

a=[5,8,87,34,56,23,11,45,88,92]
output = getSecondOrderElements(a)
print(output)
