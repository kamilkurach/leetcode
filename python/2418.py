# 2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zip1 = list(zip(names, heights))
        sorted_zip1 = sorted(zip1, key=lambda x: x[1], reverse=True) 
        return [x[0] for x in sorted_zip1]
