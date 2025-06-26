class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())