class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        if n < 3:
            return False
        
        for i in range(1, n):
            for j in range(i + 1, n):
                s1 = num[:i]
                s2 = num[i:j]
                
                if (len(s1) > 1 and s1.startswith('0')) or (len(s2) > 1 and s2.startswith('0')):
                    continue
                    
                if n - j < max(len(s1), len(s2)):
                    continue
                
                if self.isValidChain(s1, s2, num[j:]):
                    return True
                    
        return False

    def isValidChain(self, s1, s2, remaining_str):
        n1, n2 = int(s1), int(s2)
        
        while remaining_str:
            curr_sum = n1 + n2
            s_sum = str(curr_sum)
            
            if not remaining_str.startswith(s_sum):
                return False
            
            remaining_str = remaining_str[len(s_sum):]
            n1, n2 = n2, curr_sum
            
        return True