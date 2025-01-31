class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = num//3
        summ = (n-1)+n+(n+1)
        if summ == num:
            return [n-1,n,n+1]
        else:
            return []