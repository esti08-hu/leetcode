class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        [2,7,11,15]

        l, r = 0, len(numbers)-1


        '''
        l, r = 0, len(numbers)-1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l+1, r+1]
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]