from math import log10
def countDigit(num):
    return (int(log10(num)+1))

a= countDigit(3678894)
print(a)