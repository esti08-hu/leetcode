class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''

        |               |
        1,8,6,2,5,4,8,3,7
        width = len(height)-1 = 8-1
        max_ant = min(l, r) * width

        if l > r:
            r -= 1
        else:
            l += 1
        
        width -= 1


        '''

        l, r = 0, len(height) - 1
        width = len(height) - 1
        max_amt = 0
        while l < r:
            max_amt = max(max_amt, min(height[l], height[r]) * width)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
            width -= 1

        return max_amt
