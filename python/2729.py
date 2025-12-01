class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(n * 2) + str(n * 3)
        freq = [n.count(e) for e in n]
        n = sorted([int(e) for e in set(n)])
        if n == list(range(1, 10)) and sum(freq) == len(freq):
            return True
        else:
            return False
