class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        [2,1,3,3,3,2]
        2: 2 => 2//2 = 1
        1: 1 => 1//1 = 1
        3: 3 => 3//3 = 1

        1: [5]
        3: [0,1,2,3,4,6]

        res = []
        for k, v in map.items():
            j = 0
            for i in range(len(v)//k):
                curr = []
                while len(curr) <= k:
                    curr.append(v[j])
                    j+=1
                
                res.append(curr)
        '''
        group_map = defaultdict(list)
        for i, v in enumerate(groupSizes):
            group_map[v].append(i)
        
        res = []
        for k, v in group_map.items():
            j = 0
            for i in range(len(v)//k):
                curr = []
                while len(curr) < k:
                    curr.append(v[j])
                    j+=1
                res.append(curr)
        
        return res