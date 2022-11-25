class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i, e in enumerate(x):
            if x[i] != x[len(x)-1-i]:
                return False
        return True