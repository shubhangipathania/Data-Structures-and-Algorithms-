#Print 1 To N Without Loop
#using head recursion
def printNos(n):
    #Code here
    if(n==0):
        return 
    printNos(n-1)
    print(n, end=" ")

printNos(10)
# printNos(5)
# printNos(0)