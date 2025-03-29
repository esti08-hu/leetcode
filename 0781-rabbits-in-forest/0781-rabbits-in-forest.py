class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans_count = Counter(answers)

        total = 0
        for a, c in ans_count.items():
            size = a + 1
            groups = (c + a) // size
            total += (groups * size)
        
        return total