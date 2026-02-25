class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1 and bits[0]:
            return False
        i = 0
        while i < len(bits) - 1:
            if i == len(bits)-2 and bits[i] == 1:
                return False
            if bits[i] == 0:
                i+=1
            else:
                i+=2
            
        return True
