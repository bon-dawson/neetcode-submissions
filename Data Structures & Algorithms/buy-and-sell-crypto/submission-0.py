class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn, ans = prices[0], 0
        for price in prices:
            ans = max(ans, price - mn)
            mn = min(price, mn)
        return max(ans, 0)