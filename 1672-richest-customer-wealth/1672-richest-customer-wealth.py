class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in range(len(accounts)):
            if res < sum(accounts[i]):
                res = sum(accounts[i])
        return res