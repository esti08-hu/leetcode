class Solution:
    @cache
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        for i, ch in enumerate(expression):
            if ch in "+-*":
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])

                for left in left_results:
                    for right in right_results:
                        if ch == "+":
                            results.append(left + right)
                        elif ch == "-":
                            results.append(left - right)
                        else:
                            results.append(left * right)

        if not results:
            results.append(int(expression))

        return results