#Program to count the number of digits in an integer.
num=int(input("Enter the integer:"))
count=0
while (num>0):
    count=count+1
    num = num//10
print(count)