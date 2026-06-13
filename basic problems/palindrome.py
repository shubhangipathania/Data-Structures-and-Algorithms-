#program to check if a number is palindrome or not.
n=int(input("Enter the number:"))
num=n
result=0
while (num>0):
      ld=num % 10
      result = (result*10)+ld
      num= num//10
print(result)
if(result == n):
    print("The number is a palindrome number.")
else:
    print("The number is not a palindrome number.")