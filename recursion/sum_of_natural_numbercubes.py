#Given an integer n, calculate the sum of series 1**3 + 2**3 + 3**3 + 4**3 + … till n-th term.
def sumOfSeries(n):
    #code here
    if(n==0):
        return 0
    if(n==1):
        return 1 
        
    return ((n**3)+ sumOfSeries(n-1))

a= sumOfSeries(5)
print(a)