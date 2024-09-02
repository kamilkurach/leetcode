#2553. Separate the Digits in an Array
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if len(str(num)) > 1: 
                for digit in str(num):
                    result.append(int(digit))
            else:
                result.append(num)
        return result
