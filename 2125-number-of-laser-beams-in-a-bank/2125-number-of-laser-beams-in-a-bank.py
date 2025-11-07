class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        count_laser = []
        for row in bank:
            curr = row.count("1")
            if curr > 0:
                count_laser.append(curr)

        for i in range(len(count_laser)-1):
            res += (count_laser[i]*count_laser[i+1])
        return res
