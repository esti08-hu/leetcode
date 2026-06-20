class Solution:
    def mergeSimilarItems(self, items1, items2):
        totals = {}

        for value, weight in items1:
            totals[value] = totals.get(value, 0) + weight

        for value, weight in items2:
            totals[value] = totals.get(value, 0) + weight

        result = []
        for value in sorted(totals):
            result.append([value, totals[value]])

        return result