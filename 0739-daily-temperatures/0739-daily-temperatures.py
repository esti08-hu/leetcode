class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        t_dict = {}
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                idx = stk.pop()
                t_dict[idx] = i - idx
            stk.append(i)

        for k,v in t_dict.items():
            res[k] = v

        return res