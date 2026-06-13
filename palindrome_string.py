#Given a string s, return true if the string is a palindrome. Otherwise, return false.
#A string is considered a palindrome if it reads the same forwards and backwards.
def ispalindrome(s):
    left= 0
    right= len(s)-1
    while(left < right):
        if(s[left] != s[right]):
            print("False")

        left += 1
        right -= 1
    print("True")


ispalindrome("nitin")

