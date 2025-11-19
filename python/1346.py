class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # arr = sorted(arr, reverse=True)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:
                    return True
        return False
