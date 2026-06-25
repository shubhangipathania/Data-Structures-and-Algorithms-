#Given a string s, return true if the string is a palindrome. Otherwise, return false.
#A string is considered a palindrome if it reads the same forwards and backwards.
def ispalindrome(s, left, right):
    if(left >= right):
        return True
    
    if(s[left] != s[right]):
        return False
    
    else:
        return ispalindrome(s,left+1, right-1)
    
str="abcddcba"
a= ispalindrome(str, 0, len(str)-1)
print(a)

