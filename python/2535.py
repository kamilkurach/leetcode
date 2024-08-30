#2535. Difference Between Element Sum and Digit Sum of an Array
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_nums = []
        for e in nums:
            if len(str(e)) > 1:
                for v in str(e):
                    digit_nums.append(int(v))
            else:
                digit_nums.append(e)
        digit_sum = sum(digit_nums)
        return abs(element_sum - digit_sum)
