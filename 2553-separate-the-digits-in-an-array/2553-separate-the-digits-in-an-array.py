class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if num > 9:
                rem = []
                while num > 0:
                    rem.append(num%10)
                    num = num//10
                answer.extend(rem[::-1])
            else: answer.append(num)
        return answer
                

