class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = defaultdict(str)
        k = 0
        for i in range(2, 10):
            for j in range(3):
                phone[str(i)]+=(chr(k+ord('a')))
                k+=1
            if i == 7 or i == 9:
                phone[str(i)]+=(chr(k+ord('a')))
                k+=1

        res = []
        def backtrack(index, current_combination):
            if index == len(digits):
                res.append(current_combination)
                return

            letters = phone[digits[index]]

            for letter in letters:
                backtrack(index+1, current_combination+letter)
            
        backtrack(0, "")
        return res
        

        