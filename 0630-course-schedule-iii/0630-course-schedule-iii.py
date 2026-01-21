class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        curr_time = 0
        courses.sort(key=lambda x:x[1])
        max_heap = []

        for dur, lDay in courses:
            if dur > lDay:
                continue
            
            heapq.heappush(max_heap, -dur)
            curr_time += dur

            if curr_time > lDay:
                longest_dur = -heappop(max_heap)
                curr_time -= longest_dur
        
        return len(max_heap)