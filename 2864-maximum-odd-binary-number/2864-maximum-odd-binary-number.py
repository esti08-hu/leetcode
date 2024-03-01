class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        len_1 = 0
        len_0 = 0

        for char in s:
            if char == '1':
                len_1 += 1
            elif char == '0':
                len_0 += 1

        return '1' * (len_1 - 1) + '0' * len_0 + '1'