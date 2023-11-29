import re 
class Solution:
    def hammingWeight(self, n: int) -> int:
        b = format(n, 'b')
        s = re.findall('1', b)
        return len(s)
