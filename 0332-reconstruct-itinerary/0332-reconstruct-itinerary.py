class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

        "JFK","ATL","JFK","SFO","ATL","SFO"

        JFK: [SFO, ATL], SFO: [ALT], ALT: [JFK, SFO]
        JFK: [SFO, ATL], SFO: [ALT], ALT: [SFO, JFK]

        [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        MUC: [LHR], LJR: [SFO], SFO: [SJC], JFK: [MUC], LHR: [SFO]

        JFK, MUC, LHR, SFO, SJC, 
        '''
        graph = defaultdict(list)

        for f, t in tickets:
            graph[f].append(t)
        
        for f, d in graph.items():
            graph[f] = sorted(d, reverse=True)
        
        res = []
        print(graph)
        def dfs(f):
            while graph[f]:
                curr = graph[f].pop()
                dfs(curr)
            res.append(f)
        dfs("JFK")
        return res[::-1]