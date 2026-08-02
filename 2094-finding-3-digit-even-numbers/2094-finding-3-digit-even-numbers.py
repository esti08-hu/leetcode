class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k and not digits[k]%2:
                        digit = int("".join(map(str,[digits[i], digits[j], digits[k]])))
                        res.add(digit)
        
        return sorted(list(res))