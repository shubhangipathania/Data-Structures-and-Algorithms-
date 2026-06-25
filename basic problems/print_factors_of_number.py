#Program to print the factors of a number
from math import sqrt
#Brute Force
# num=int(input("Enter the number:"))
# result=[]
# for i in range(1,num+1):
#     if(num % i == 0):
#         result.append(i)

# print(result)
# print(len(result))

#Better Solution
# num2= int(input("Enter the number:"))
# result2=[]
# for i in range(1,(num2//2)+1):
#     if(num2 % i == 0):
#         result2.append(i)
# result2.append(num2)
# print(result2)
# print(len(result2))

#optimal Solution
num3= int(input("Enter the number:"))
result3= []
for i in range(1, int(sqrt(num3))+1):
    if(num3 % i == 0):
        result3.append(i)
        if(num3//i != i):
            result3.append(num3//i)
result3.sort()
print(result3)

