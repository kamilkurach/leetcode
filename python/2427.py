# 2427. Number of Common Factors
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for i in range(1, 1001):
            if i <= a or i <= b:
                if a % i == 0 and b % i == 0:
                    count += 1 
        return count
