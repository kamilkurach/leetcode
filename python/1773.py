class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            typeValue = item[0]
            colorValue = item[1]
            nameValue = item[2]
            if ruleKey == "type" and ruleValue == typeValue:
                count+=1
            elif ruleKey == "color" and ruleValue == colorValue:
                count+=1
            elif ruleKey == "name" and ruleValue == nameValue:
                count+=1
        return count
