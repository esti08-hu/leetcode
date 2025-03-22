class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero_count = [0]
        one_count = [0]
        count0= 0
        for n in nums:
            if n == 0:
                count0+=1
                zero_count.append(count0)
            else:
                zero_count.append(count0)
        count1 = 0
        for n in nums[::-1]:
            if n == 1:
                count1+=1
                one_count.append(count1)
            else:
                one_count.append(count1)
        max_sum = float("-inf")
        res = []
        one_count = one_count[::-1]

        for i in range(len(zero_count)):
            curr = zero_count[i] + one_count[i]
            
            if curr > max_sum:
                res = []
                max_sum =curr
                res.append(i)
            elif curr == max_sum:
                res.append(i)
        return res