class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if nums.count(i) > len(nums)/3:
                if i not in result:
                    result.append(i)
        return result
