#program to store the frequency in the dictionary.
nums=[2,6,74,2,1,2,7,5,9,6]
freq_map={}
for i in range(0,len(nums)):
    if(nums[i] in freq_map):
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)
print(freq_map[2])


nums2=[4,7,8,3,45,6,7,3,2,4]
hash_map={}
n=len(nums2)
for i in range(0,n):
    hash_map[nums2[i]] = hash_map.get(nums2[i],0) + 1

print(hash_map)