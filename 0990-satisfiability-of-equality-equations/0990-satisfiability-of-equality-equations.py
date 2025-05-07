class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
                parent[rx] = ry
        for eq in equations:
            if eq[1] == "=":
                union(ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a"))
        for eq in equations:
            if eq[1] == "!":
                if find(ord(eq[0]) - ord("a")) == find(ord(eq[3]) - ord("a")):
                    return False
        return True

