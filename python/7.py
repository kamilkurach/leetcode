class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if "-" in x:
            x = x.replace("-", "")
            x = "-" + x
        if int(x) < -2147483648 or int(x) > 2147483647:
            return 0
        else:
            return int(x)