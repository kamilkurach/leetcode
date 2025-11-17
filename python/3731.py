class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        gt_nums = list(range(min(nums), max(nums) + 1))
        return sorted(list(set(gt_nums).difference(set(nums))))
