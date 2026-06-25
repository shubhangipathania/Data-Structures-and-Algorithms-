#Print numbers from n to 1 (space separated) without the help of loops.
def printNos(n):
    # Code here
    if(n==0):
        return
        
    print(n, end=" ")
    printNos(n-1)


printNos(10)