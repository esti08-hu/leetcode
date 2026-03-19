class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dist_sum = sum(distance)
        x = sum(distance[start:destination])

        return min(dist_sum - x, x)