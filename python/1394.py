#1394. Find Lucky Integer in an Array
def findLucky(self, arr: List[int]) -> int:
        temp = []
        for e in arr:
            if arr.count(e) == e:
                temp.append(e)
        if len(temp) != 0:
            return max(temp)
        else:
            return -1
