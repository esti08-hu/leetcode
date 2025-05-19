class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for n in encoded:
            res.append(res[-1] ^ n)
        return res