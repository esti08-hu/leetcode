class Solution:
    def largestTimeFromDigits(self, arr):
        best_time = -1
        answer = ""

        for p in permutations(arr):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]

            if hour < 24 and minute < 60:
                total = hour * 60 + minute

                if total > best_time:
                    best_time = total
                    answer = f"{hour:02d}:{minute:02d}"

        return answer