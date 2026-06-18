class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            even = []
            odd = []

            for i, ch in enumerate(word):
                if i % 2 == 0:
                    even.append(ch)
                else:
                    odd.append(ch)

            even.sort()
            odd.sort()

            key = (tuple(even), tuple(odd))

            groups.add(key)

        return len(groups)