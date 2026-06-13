def isArmstrong(num):
    # Write your code here.
    x = (num)
    total = 0
    count = 0 
    original = num
    while(x>0):
        count += 1
        x = x // 10

    while (num >0):
        last_digit = num % 10
        last_digit = (last_digit)**count
        total= total + last_digit
        num = num // 10

    if (total == original):
        return 'yes'
    else:
        return 'no'
