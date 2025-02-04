class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] != 9:
        #     digits[-1]=digits[-1]+1
        # else:
        s = ''
        dl = []
        digits[-1]=digits[-1]+1
        for d in digits:
            s+=str(d)
        for c in s:
            dl.append(int(c))
        return dl

        # return digits