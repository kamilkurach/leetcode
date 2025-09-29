class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_divisible = []
        divisible = []
        for i in range(1, n+1):
            if i%m != 0:
                not_divisible.append(i)
            else:
                divisible.append(i)
        return sum(not_divisible) - sum(divisible)
