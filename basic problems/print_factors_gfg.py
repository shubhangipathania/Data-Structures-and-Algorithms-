from math import sqrt
class Solution:
    def countFactors (self, n):
        # code here
        result=[]
        for i in range(1, int(sqrt(n)) +1 ):
            if(n % i == 0):
                result.append(i)
                if(n//i != i):
                    result.append(n//i)
                    
        print(len(result)) 


s1=Solution()
s1.countFactors(36)  