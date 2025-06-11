class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = defaultdict(list)
        for u, v in richer:
            adj[v].append(u)
        n = len(quiet)
        answer = [-1] * n

        def dfs(node):
            if answer[node] != -1:
                return answer[node]
            min_person = node
            for richer_person in adj[node]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[min_person]:
                    min_person = candidate
            answer[node] = min_person
            return min_person

        for i in range(n):
            if answer[i] == -1:
                dfs(i)
        return answer