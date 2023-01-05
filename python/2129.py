class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        arr = title.split()
        result = []
        for e in arr:
            if len(e) > 2:
                result.append(e.capitalize())
            else:
                result.append(e)
        return " ".join(result)
        