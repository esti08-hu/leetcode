class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num = [i+1 for i in range(n)]
        if n > time:
            return num[time]
        num_1 = time-n
        num_2 = num_1//(n-1)
        rem = num_1%(n-1)
        
        if num_2%2==0 or num_2==0:
            return (num[-rem-2])
        else:
            return num[rem]