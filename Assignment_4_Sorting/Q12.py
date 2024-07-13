class Solution:
    def buyTwoChocolates(self, prices: List[int], money: int) -> bool:
        prices.sort()
        return prices[0] + prices[1] <= money


sol = Solution()
prices = [1,2,2]
money = 3
print(sol.buyTwoChocolates(prices, money))  
