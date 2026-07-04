class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        n = len(arr)
        five_per = (n*5) // 100

        return sum(arr[0+five_per:n-five_per])/(n-(five_per*2))