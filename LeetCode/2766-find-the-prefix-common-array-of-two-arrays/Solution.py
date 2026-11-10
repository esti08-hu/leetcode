class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            curr_set = set(A[:i+1])
            count = 0
            for j in range(i+1):
                if B[j] in curr_set:
                    count += 1
            res.append(count)
        return res
