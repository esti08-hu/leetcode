class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        t_dict = {}
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                t_dict[idx] = i - idx
                res[idx] = i - idx
            stk.append(i)

        return res