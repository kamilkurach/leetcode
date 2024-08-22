#Binary Number with Alternating Bits
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = ""
        for bit in bin(n)[2:]:
            if bit == "0" and prev == "" or bit == "1" and prev == "":
                prev = bit
            elif bit == "0" and prev == bit or bit == "1" and prev == bit:
                return False
            else:
                prev = bit
        return True
