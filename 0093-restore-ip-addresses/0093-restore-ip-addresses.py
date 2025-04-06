class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, dots, curr_ip):
            if dots == 4:
                if start == len(s):
                    res.append(curr_ip[:-1])
                return 
            if start == len(s):
                return
            
            for i in range(start, min(start+3, len(s))):
                curr = s[start:i+1]
                if (curr.startswith("0") and len(curr) > 1) or int(curr) > 255:
                    continue 
                
                backtrack(i + 1, dots + 1, curr_ip + curr + ".")
        
        backtrack(0,0,"")
        return res