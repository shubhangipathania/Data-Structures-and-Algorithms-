#Given a positive number n, print the string "GFG" exactly n times separated by a single space.
n=int(input())
def funcgfg(n):
    if (n==0):
        return 
    if(n==1):
        print("GFG")
        return
    print("GFG", end=" ")
    funcgfg(n-1)


funcgfg(n)

