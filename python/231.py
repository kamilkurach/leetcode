class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 0
        count = 0
        while p <= n:
            p = pow(2, count)
            count+=1
            if p == n:
                return True
        return False