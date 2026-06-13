#program to count the no of times the str in q appears in s.
#brute force
# s="azyxyyzaaaa"
# q=['d','a','y','x']
# for ch in q:
#     count=0
#     for w in s:
#         if(w == ch):
#             count += 1
#     print(count)

#optimal Solution
s="azyxyyzaaaa"
q=['d','a','y','x']
hash_list=[0]*26
for ch in s:
    ascii_value= ord(ch)
    index= ascii_value - 97
    hash_list[index] += 1

for ch in q:
    ascii_value = ord(ch)
    index= ascii_value - 97
    print(hash_list[index])