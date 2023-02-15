class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        current_max = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                diff = prices[right] - prices[left]
                current_max = max(current_max, diff)
            right += 1
        return current_max
