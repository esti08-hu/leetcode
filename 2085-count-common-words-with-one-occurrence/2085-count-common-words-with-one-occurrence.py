class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_cnt = Counter(words1)
        words2_cnt = Counter(words2)
        count = 0

        for k, v in words1_cnt.items():
            if v == 1 and words2_cnt[k] == 1:
                count += 1
        
        return count