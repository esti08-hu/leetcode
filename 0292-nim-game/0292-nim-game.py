class Solution:
    def canWinNim(self, n: int) -> bool:
        '''
        5 
        1 1 3
        5
        8 -> 2 1 1 
        4

        3
        2
        1
        
        '''
        if not n%4:
            return False
        return True