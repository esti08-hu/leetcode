class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        oprators = ['+', '-', '*', '/']
        for t in tokens:
            if t not in oprators:
                stk.append(int(t))
            else:
                if len(stk)>=2:
                    n2 = stk.pop()
                    n1 = stk.pop()
                else:
                    continue

                if t == "+":
                    stk.append(n1+n2)
                elif t == "-":
                    stk.append(n1-n2)
                elif t == "/":
                    stk.append(int(n1/n2))
                else:
                    stk.append(n1*n2)
                
        return stk[-1]