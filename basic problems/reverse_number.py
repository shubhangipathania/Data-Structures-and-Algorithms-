#Program to reverse a number(positive and negative both)

class Solution(object):
    def reverse(self, x):
        num=abs(x)
        result=0
        while(num>0):
            last_digit = num % 10
            result=(result*10) + last_digit
            num=num//10
        
        if(x<0):
            result = -result
        if(result < -2**31 or result > (2**31) -1):
            print("zero")

        print(result)
        

a1=Solution()
a1.reverse(561)
a1.reverse(-123)