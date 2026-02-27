class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def str_dict(word):
            lp_count = {}
            for c in word:
                if c.isalpha():
                    c_ = c.lower()
                    lp_count[c_] = lp_count.get(c_, 0) + 1
            return lp_count

        lp = str_dict(licensePlate)
        result = None

        for word in words:
            curr = str_dict(word)
            if all(curr.get(ch, 0) >= count for ch, count in lp.items()):
                if result is None or len(word) < len(result):
                    result = word

        return result