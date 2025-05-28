class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        stack = []
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        