class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = sum(arr)
        pre = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pre[i+1] = pre[i] + arr[i]

        for i in range(3, len(pre), 2):
            r = i
            l = 0
            while r < len(pre):
                total += (pre[r] - pre[l])
                r += 1
                l += 1
        
        return total