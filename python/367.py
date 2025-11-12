class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num**(1/2)) * int(num**(1/2)) == num:
            return True 
        else:
            return False
