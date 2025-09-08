class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            curr = []
            while n > 0:
                curr.append(n%10)
                n //= 10
            curr.reverse()
            res.extend(curr)
        return res

