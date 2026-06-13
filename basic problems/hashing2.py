n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_map={}
for num in n:
   hash_map[num]= hash_map.get(num,0)+1

for num in m:
   if(num in hash_map):
      print(hash_map[num])
   else:
      print(0)