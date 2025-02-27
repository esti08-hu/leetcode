from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        freq = list(c.values())  
        
        for i in range(len(freq)):
            freq[i] -= 1  
            
            if freq[i] == 0:
                temp_freq = freq[:i] + freq[i+1:]
            else:
                temp_freq = freq
            
            if len(set(temp_freq)) == 1: 
                
                return True
            
            freq[i] += 1  
            
        return False
