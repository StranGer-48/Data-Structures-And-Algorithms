def buy_and_sell_stock_twice(prices):
    min_price_so_far, max_total_profit = float('inf'), 0.0
    first_buy_sell_profits = [0] * len(prices)

    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price-min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far-price + first_buy_sell_profits[i-1]
        )
    return max_total_profit

A = [12,11,13,9,12,8,14,13,15]
print(buy_and_sell_stock_twice(A))