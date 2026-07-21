class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_idx = None
        if ruleKey == "type":
            key_idx = 0
        elif ruleKey == "color":
            key_idx = 1
        else:
            key_idx = 2
        
        count = 0
        for item in items:
            if item[key_idx] == ruleValue:
                count += 1
        
        return count