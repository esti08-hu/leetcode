class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num%3 != 0:
                res+=1
        return res

        """
        res = 0
        num % 3 
        possibilities 0 1 2
        """