class Solution:
    # 10:39
    def maxProfit(self, prices: List[int]) -> int:

        b = 0
        max_diff = 0
        for s in range(len(prices)):
            if prices[b] > prices[s]:
                b = s
            else:
                diff = prices[s] - prices[b]
             
                if diff > max_diff:
                    max_diff = diff
            
        return max_diff