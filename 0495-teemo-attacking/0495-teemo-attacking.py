class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_set = set()

        for t in timeSeries:
            time_set.add(t)
            time_set.add(t+1)
            
        return len(time_set)