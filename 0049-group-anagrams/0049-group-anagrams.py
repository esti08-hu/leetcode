class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            key = tuple(count)
            anagrams.setdefault(key, []).append(word)
        return list(anagrams.values())