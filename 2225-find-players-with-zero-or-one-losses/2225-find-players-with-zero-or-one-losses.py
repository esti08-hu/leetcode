from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = []
        loss = []
        for l in matches:
            win.append(l[0])
            loss.append(l[1])
        count_loss = Counter(loss)
        res1 = []

        for key, value in count_loss.items():
            if value == 1:
                res1.append(key)

        win_set = set(win)
        loss_set = set(loss)
        ans = []
        res = []
        for w in win_set:
            if w not in loss_set:
                res.append(w)

        ans.append(sorted(res))
        ans.append(sorted(res1))
        return ans

