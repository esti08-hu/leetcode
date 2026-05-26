class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_city = set()
        for start, dest in paths:
            start_city.add(start)
        
        for start, dest in paths:
            if dest not in start_city:
                return dest