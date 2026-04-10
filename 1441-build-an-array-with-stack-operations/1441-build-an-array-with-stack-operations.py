class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        j = 0

        for i in range(1, n+1):
            if i != target[j]:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
                j+=1
            
            if i == target[-1]:
                return res