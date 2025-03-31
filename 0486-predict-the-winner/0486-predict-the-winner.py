class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(start, end, player1_turn):
            if start > end:
                return 0

            if player1_turn:
                pick_start = nums[start] + helper(start + 1, end, False)
                pick_end = nums[end] + helper(start, end - 1, False)
                return max(pick_start, pick_end)
            else:
                pick_start = helper(start + 1, end, True)
                pick_end = helper(start, end - 1, True)
                return min(pick_start, pick_end)

        total_sum = sum(nums)

        p1_score = helper(0, len(nums) - 1, True)
        p2_score = total_sum - p1_score

        return p1_score >= p2_score