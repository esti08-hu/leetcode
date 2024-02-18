from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability = [0] * n
        meeting_count = [0] * n

        for start, end in sorted(meetings):
            min_avail_time = float('inf')
            min_avail_room = 0
            found_unused_room = False

            for i in range(n):
                if room_availability[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability[i] = end
                    break

                if min_avail_time > room_availability[i]:
                    min_avail_time = room_availability[i]
                    min_avail_room = i

            if not found_unused_room:
                room_availability[min_avail_room] += end - start
                meeting_count[min_avail_room] += 1

        return meeting_count.index(max(meeting_count))