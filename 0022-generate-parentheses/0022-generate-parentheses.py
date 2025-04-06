class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(res, curr, open_count, close_count, max_pairs):
            if open_count == max_pairs and close_count == max_pairs:
                res.append("".join(curr))
                return
            if open_count < max_pairs:
                curr.append("(")
                backtrack(res, curr, open_count + 1, close_count, max_pairs)
                curr.pop()
            
            if close_count < open_count:
                curr.append(")")
                backtrack(res, curr, open_count, close_count + 1, max_pairs)
                curr.pop()
        res = []

        backtrack(res, [], 0, 0, n)
        return res
