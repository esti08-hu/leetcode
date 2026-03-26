class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = math.prod(nums)
        if prod == 0:
            answer = [0]*len(nums)
            zero = [0, 0]
            p = 1

            for i in range(len(nums)):
                if nums[i] == 0:
                    zero[0] += 1
                    if zero[0] > 1:
                        return answer
                    zero[1] = i
                else:
                    p *= nums[i]
            answer[zero[1]] = p

            return answer
        else:
            answer = []
            for num in nums:
                answer.append(prod//num)
            return answer