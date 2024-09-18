import math

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        tab = []
        count=0
        for e in nums:
            if e % 2 == 0 and e % 3 == 0:
                tab.append(e)
                count+=1
        if len(tab) > 0:
            return math.floor(sum(tab)/count)
        else:
            return 0
