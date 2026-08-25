class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = []
        friends_set = set(friends)
        for o in order:
            if o in friends_set:
                res.append(o)
        return res