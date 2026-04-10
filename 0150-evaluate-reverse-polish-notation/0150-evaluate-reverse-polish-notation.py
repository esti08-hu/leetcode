class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        oprators = {"-", "+", "*", "/"}

        for token in tokens:
            if token not in oprators:
                stk.append(int(token))
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                if token == "+":
                    stk.append(num1 + num2)
                elif token == "-":
                    stk.append(num1 - num2)
                elif token == "*":
                    stk.append(num1 * num2)
                else:
                    if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
                        stk.append(num1 // num2)
                    else:
                        if num1 < 0:
                            num1 *= -1
                        else:
                            num2 *= -1
                        stk.append(-(num1 // num2))
                        
        return stk[-1]


