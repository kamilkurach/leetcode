class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        product_of_digits = int(s[0])
        sum_of_digits = int(s[0])
        for e in s[1:]:
            product_of_digits = product_of_digits * int(e)
            sum_of_digits = sum_of_digits + int(e)
        return product_of_digits - sum_of_digits
        
