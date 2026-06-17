class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        p_cnt = len(Counter(pattern))
        for word in words:
            chr_map = {}
            if len(Counter(word)) != p_cnt:
                continue
            for i in range(len(word)):
                if word[i] not in chr_map:
                    chr_map[word[i]] = pattern[i]
                else:
                    if chr_map[word[i]] != pattern[i]:
                        break
            else:
                res.append(word)
        
        return res