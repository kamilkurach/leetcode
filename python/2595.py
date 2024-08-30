#2595. Number of Even and Odd Bits
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        binary = reversed(list(bin(n))[2:]) -> reversed index order? :/
        for i, e in enumerate(binary):
            if e == '1' and i%2 == 0:
                even+=1
            elif e == '1' and i%2 != 0:
                odd+=1
        return [even, odd]
