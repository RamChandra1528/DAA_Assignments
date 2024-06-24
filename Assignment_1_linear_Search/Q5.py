def richest_customer_wealth(accounts):
    max_wealth = 0
    for account in accounts:
        wealth = sum(account)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth


accounts = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
print(richest_customer_wealth(accounts))
