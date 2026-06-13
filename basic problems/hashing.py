#program to count the times the elements of m is occuring in n 
#brute force
# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]
# for num in m:
#     count=0
#     for x in n:
#         if(x==num):
#             count += 1
#     print(count)

#optimal Solution 
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for num in n:
    hash_list[num] += 1
for num in m:
   if(num<0 or num>10):
       print(0)
   else:
       print(hash_list[num])