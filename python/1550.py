class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        marked_arr = ""
        for x in arr:
            if x % 2 == 1:
                marked_arr = marked_arr + "1"
            else:
                marked_arr = marked_arr + "0"
        
        for e in marked_arr.split("0"):
            if '111' in e:
                return True
        
        return False
