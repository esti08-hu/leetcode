class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                 '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        combination = [""]

        for digit in digits:
            new_combination = []
            for comb in combination:
                letters = phone[digit]
                for letter in letters:
                    new_combination.append(comb+letter)
            
            combination = new_combination
        
        return combination



        
        

        