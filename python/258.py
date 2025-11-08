class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            tmp = 0
            for e in str(num):
                tmp += int(e)
            num = tmp
        return num
