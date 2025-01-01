#476. Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        c1 = str(bin(num)[:2])
        c2 = ""
        for e in str(bin(num)[2:]):
            if e == "0":
                c2 = c2 + "1"
            else:
                c2 = c2 + "0"
        c = c1 + c2
        
        return int(c, 2)
