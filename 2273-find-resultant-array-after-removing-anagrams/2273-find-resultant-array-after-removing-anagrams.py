class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev = words[0]
        prev_cnt = Counter(prev)
        res.append(prev)

        for i in range(1, len(words)):
            curr = words[i]
            curr_cnt = Counter(curr)

            if prev_cnt != curr_cnt:
                res.append(curr)
                prev = curr
                prev_cnt = curr_cnt

        return res
