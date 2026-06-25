#Program to check if a number is an armstrong number or not.
n=int(input("Enter the number:"))
num = n
count=0
total=0
# nod=len(str(num))
while (num>0):
    count = count+1
    num = num//10
print(count)

num = n
while (num>0):
    ld=num % 10
    ld= ld**count 
    total=total + ld
    num=num//10
print(total)
if (total==n):
    print("It is an Armstrong number.")
else:
    print("It is not an armstrong number.")


