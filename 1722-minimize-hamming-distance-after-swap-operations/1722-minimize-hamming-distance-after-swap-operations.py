class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in allowedSwaps:
            rootA = find(a)
            rootB = find(b)
            if rootA != rootB:
                parent[rootB] = rootA

        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        hamming_distance = 0
        for indices in groups.values():
            source_count = Counter(source[i] for i in indices)
            target_count = Counter(target[i] for i in indices)
            for val in target_count:
                matched = min(source_count[val], target_count[val])
                source_count[val] -= matched
            hamming_distance += sum(source_count.values())

        return hamming_distance