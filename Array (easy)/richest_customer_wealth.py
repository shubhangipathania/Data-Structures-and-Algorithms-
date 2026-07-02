#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
#Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts.
# The richest customer is the customer that has the maximum wealth.
def richest_customer_wealth(accounts):
    total_money = 0
    max_money = 0
    for i in range(len(accounts)):
        for j in range(len(accounts[i])):
            total_money = total_money + accounts[i][j]
        max_money = max(total_money,max_money)
        total_money = 0

    return max_money 


accounts= [[1,2,3],[3,2,1]]
output = richest_customer_wealth(accounts)
print(output)