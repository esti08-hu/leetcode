class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = str(nums[0]) 
        right = left
        res = [] 

        for num in nums[1:]:
            if num - int(right) == 1:
                right = str(num)
            else:
                if right != left:
                    res.append(left + "->" + right)
                else:
                    res.append(left)

                left = str(num)
                right = left
        
        if right != left:
            res.append(left + "->" + right)
        else:
            res.append(left)
            
        return res