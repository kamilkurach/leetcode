class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        result = []
        for e in digits:
            num = num + str(e)
        temp_num = int(num) + 1
        for e in list(str(temp_num)):
            result.append(int(e))
        return result
