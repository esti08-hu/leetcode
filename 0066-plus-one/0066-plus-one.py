class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        cr = 1
        for i in range(n-1, -1, -1):
            if cr == 0:
                break
            new = digits[i] + cr
            if new == 10:
                digits[i] = 0
                cr = 1
            else:
                digits[i] = new
                cr = 0
        if cr == 1:
            digits.insert(0, 1)
        return digits