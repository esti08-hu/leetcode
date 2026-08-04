class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, 0
        if colors[0] != colors[-1]:
            return len(colors) - 1
        for i in range(len(colors)):
            if colors[-1] != colors[i]:
                l = i + 1
                break

        for j in range(len(colors)-1, -1, -1):
            if colors[0] != colors[j]:
                r = len(colors) - j
                break

        print(r, len(colors) - l, l)
        return len(colors) - min(r, l)