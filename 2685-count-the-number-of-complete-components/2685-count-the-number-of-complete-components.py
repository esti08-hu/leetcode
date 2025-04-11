class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph= defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, component):
            visited.add(node)
            component.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        def is_comp(comonent):
            size = len(component)
            edges = sum(len(graph[node]) for node in component) // 2

            return edges == size*(size - 1)//2

        count = 0
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)
                if is_comp(component):
                    count+=1

        return count
