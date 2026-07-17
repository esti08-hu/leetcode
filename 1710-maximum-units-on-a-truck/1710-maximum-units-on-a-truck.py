class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sortedBTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        total_units = 0

        for i in range(len(sortedBTypes)):
            if truckSize > sortedBTypes[i][0]:
                total_units += sortedBTypes[i][0]  * sortedBTypes[i][1]
                truckSize -= sortedBTypes[i][0]
            else:
                total_units += truckSize * sortedBTypes[i][1]
                break

        return total_units