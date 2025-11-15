class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        n = len(wordList)

        for i in range(n-1):
            for j in range(i+1, n):
                cnt = 0
                for k in range(len(wordList[j])):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1
                if cnt == 1:
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        path = 1
        while q:            
            for i in range(len(q)):
                node = q.popleft()
                for nei in adjList[node]:
                    if nei == endWord:
                        return path + 1
                    if nei not in visited:
                        q.append(nei)   
                        visited.add(nei)
            
            path+=1
        return 0

