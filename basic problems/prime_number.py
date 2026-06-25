#Given a number n, determine whether it is a prime number or not.
#Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

from math import sqrt
def isPrime(n):
    # code here
    count=0
    if (n<1 or n==1):
        return False
            
    for i in range(1, int(sqrt(n))+1):
        if ((n % i)== 0) :
            count += 1
                
    if(count==2):
        return False
    elif(count==1):
        return True
    else:
        return False
    
a=isPrime(10)
print(a)
            
            
        