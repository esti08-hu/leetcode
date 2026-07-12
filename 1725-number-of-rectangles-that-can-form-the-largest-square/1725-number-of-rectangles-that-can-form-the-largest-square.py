class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        min_dict = defaultdict(int)
        for l, w in rectangles:
            min_dict[min(l, w)] += 1
        
        maxVal = max(min_dict.keys())
        return min_dict[maxVal]