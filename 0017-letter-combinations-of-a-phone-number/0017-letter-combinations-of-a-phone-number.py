class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = defaultdict(str)
        k = 0
        for i in range(2, 10):
            for j in range(3):
                phone_dict[str(i)]+=(chr(k+ord('a')))
                k+=1
            if i == 7 or i == 9:
                phone_dict[str(i)]+=(chr(k+ord('a')))
                k+=1
        combination = [""]    

        for digit in digits:
            new_comb = []
            for com in combination:
                for letter in phone_dict[digit]:
                    new_comb.append(com+letter)
            
                combination = new_comb
        
        return combination
        

        