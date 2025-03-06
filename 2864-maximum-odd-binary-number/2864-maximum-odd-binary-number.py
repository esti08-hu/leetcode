class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)

        s.sort()

        if s[-1]=="1":
            s.remove(s[-1])
            s = s[::-1]

            s.append(1)
                            
        return "".join(map(str, s))