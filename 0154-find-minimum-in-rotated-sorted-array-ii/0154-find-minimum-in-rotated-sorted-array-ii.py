class Solution:
    def findMin(self, nums: List[int]) -> int:
      '''
      0 1 2 3 4 5 6
      0,1,4,4,5,6,7
           
      1 => 1,4,4,5,6,7,0
      2 => 4,4,5,6,7,0,1
      3 => 4,5,6,7,0,1,4
    
      1 1 1 2 3 3 4 5 6 6
      |                 |
      3 3 4 5 6 6 1 1 1 2
      1 1 1 2 3

      1 1 2 3 1

      2 3 1 1 1
      l   m   r
      1 1 1 4 1
      1
      mid = 6
      r = 2
      l = 3
      '''  
      return min(nums)