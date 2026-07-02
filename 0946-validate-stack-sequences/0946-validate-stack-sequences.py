class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 0

        for num in pushed:
            stk.append(num)

            while stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1
            
        return i == len(pushed)