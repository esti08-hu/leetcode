class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(m):
            dic = ["", 0]
            prev = ["", 0]
            l = i
            r = i + m
            while r <= len(arr):
                curr = [",".join(map(str, arr[l:r])), l]
                if prev[0] == curr[0]:
                    dic[1] += 1
                else:
                    dic[0] = curr[0]
                    dic[1] = 1
                
                if dic[1] == k:
                    return True
                l += m
                r += m
                prev = curr

        return False