class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_s = strs[0]
        for s in range(len(min_s)):
            i=0
            count = 0
            while(i<len(strs)):
                if min_s[s] != strs[i][s]:
                    return res
                else:
                    count+=1
                i+=1
            if count == len(strs):
                res+=min_s[s]

        return res

