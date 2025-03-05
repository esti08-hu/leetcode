class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split("/")

        stk = []

        for p in split_path:
            if p.isalpha():
                stk.append(p)
            elif p == ".." and stk:
                stk.pop()
            elif p != "" and  p != "." and p != "..":
                stk.append(p)
            
        return "/"+"/".join(map(str, stk))