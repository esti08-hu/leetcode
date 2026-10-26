class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[11]) > 6:
                count += 1
            elif int(detail[11]) == 6 and int(detail[12]) > 0:
                count += 1

        return count
            