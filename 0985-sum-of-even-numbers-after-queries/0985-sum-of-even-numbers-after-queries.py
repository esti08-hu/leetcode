class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_nums = [x for x in nums if x%2 == 0]

        for q in queries:
            if nums[q[1]] % 2 == 0:
                even_nums.remove(nums[q[1]])
                
            nums[q[1]] += q[0]

            if nums[q[1]] % 2 == 0:
                even_nums.append(nums[q[1]])
            
            res.append(sum(even_nums))
        
        return res 