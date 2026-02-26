class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if ord(target) - ord(letters[i]) < 0:
                return letters[i]
        return letters[0]