class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            window_count = Counter(s2[left:right+1])
            if not s1_counter - window_count:
                return True 
            else:
                left+=1
                right+=1

        return False
