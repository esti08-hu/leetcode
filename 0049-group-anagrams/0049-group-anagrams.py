class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for s in strs:
            curr = []
            for c in s:
                curr.append(c)
            curr.sort()
            curr = "".join(curr)
            if curr not in hashMap:
                hashMap[curr].append(s)
            else:
                hashMap[curr].append(s)
        
        res = []
        for v in hashMap.values():
            res.append(v)
        
        return res
