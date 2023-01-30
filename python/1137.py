class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            for e in range(3, n+1):
                arr.append(arr[e-1] + arr[e-2] + arr[e-3])
            return arr[-1]
