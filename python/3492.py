class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        capacity = n*n
        if capacity*w <= maxWeight:
            return capacity
        else:
            return maxWeight // w
