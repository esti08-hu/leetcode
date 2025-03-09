class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []

        for l in logs:
            if stk and l=="../":
                stk.pop()
            else:
                if l == "./" or l == "../":
                    continue
                else:
                    stk.append(l)
        return len(stk)
