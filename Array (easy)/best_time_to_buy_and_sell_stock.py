#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#brute Force
def best_time_to_buy_stock(price):
    n = len(price)
    maximum_profit = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if(price[j] > price[i]):
                p = price[j] - price[i]
                maximum_profit = max(maximum_profit, p)

    return maximum_profit

price = [7,2,1,5,6,4,8]
output = best_time_to_buy_stock(price)
print(output)


#optimal solution 
def best_time_to_buy_and_sell_stock(prices):
    n = len(prices)
    max_profit = 0 
    min_price = float("inf")
    for i in range(0,n):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price) 

    return max_profit


prices = [7,2,1,5,6,4,8]
output2 = best_time_to_buy_and_sell_stock(prices)
print(output2)