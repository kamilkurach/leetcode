#2778. Sum of Squares of Special Elements 
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        special_nums = []
        for i, e in enumerate(nums):
            i+=1
            if len(nums)%i == 0:
                special_nums.append(e)
        return sum([e*e for e in special_nums])
