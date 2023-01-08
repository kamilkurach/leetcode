class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = []
        min_val = prices[0]
        for e in prices:
            d = e - min_val
            result.append(d)
            if e < min_val:
                min_val = e 
        return max(result)
        