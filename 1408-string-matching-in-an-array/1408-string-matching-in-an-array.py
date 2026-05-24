class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[i]) > len(words[j]) or words[i] == words[j]:
                    continue
                
                if words[i] in words[j]:
                    res.add(words[i])
                    break
            
        return list(res)
                

