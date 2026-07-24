class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        curr_ex = initialExperience 
        curr_en = initialEnergy

        res = 0
        total_en = sum(energy)
        if total_en >= initialEnergy:
            res += total_en - initialEnergy + 1
        
        for i in range(len(experience)):
            if curr_ex <= experience[i]:
                curr = experience[i] - curr_ex + 1
                curr_ex += curr + experience[i]
                res += curr
            else:
                curr_ex += experience[i]
        
        return res