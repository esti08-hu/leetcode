class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dic = defaultdict(int)
        pre = [0] * (len(arr) +1)
        for i in range(1,len(arr)+1):
            pre[i] = pre[i-1]+arr[i-1]

        n = len(arr)//2
        for i in range(1, n+1):
            dic[i]= 0
            l, r = 0, i-1

            while r <= len(arr)-1:

                if target == pre[r+1] - pre[l]:
                    dic[i] += 1
                l+=1
                r+=1

            if dic[i] >= 2:
                return dic[i]
        return -1