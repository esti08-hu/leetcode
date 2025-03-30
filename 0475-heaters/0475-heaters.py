class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def find(heaters, house):
            left, right = 0, len(heaters)-1
            min_radius = float('inf')
            while left<=right:
                mid = (left+right)//2
                min_radius = min((min_radius, abs(heaters[mid]-house)))
                if heaters[mid] < house:
                    left = mid+1
                else:
                    right = mid-1
            return min_radius
        
        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius, find(heaters, house))
        return radius
