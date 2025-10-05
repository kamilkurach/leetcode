class Solution:
    def bitwiseComplement(self, n: int) -> int:
        f = ""
        for e in bin(n)[2:]:
            if e == "1":
                f = f + "0"
            else:
                f = f + "1"
        return int(f, 2)
