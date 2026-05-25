class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        if str(x) in str(n) and str(n)[0] != str(x):
            return True
        else: 
            return False
