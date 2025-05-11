class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]
        
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                if rx < ry:
                    parent[ry] = rx
                else:
                    parent[rx] = ry
        
        for a, b in zip(s1, s2):
            union(ord(a) - ord("a"), ord(b) - ord("a"))
        
        res = ""
        for char in baseStr:
            res += chr(find(ord(char) - ord("a")) + ord("a"))
        
        return res