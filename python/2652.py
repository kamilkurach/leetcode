#2652. Sum Multiples
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        tab = []
        for i in range(1, n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                tab.append(i)
        return sum(tab)
