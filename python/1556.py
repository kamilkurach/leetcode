class Solution:
    def thousandSeparator(self, n: int) -> str:
        count=1
        result = str(n)
        i=len(str(n))-1
        if len(str(n)) <= 3:
            return str(n)
        else:
            while i > 0:
                if count == 3:
                    result = result[:i] + "." + result[i:]
                    count=0
                i-=1
                count+=1
            return result
            