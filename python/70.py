class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        for e in range(2, n+1):
            arr.append(arr[e-1] + arr[e-2])

        return arr[-1]
