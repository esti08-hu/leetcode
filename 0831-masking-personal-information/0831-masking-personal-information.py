class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            idx = s.index("@")
            return s[0].lower() + "*****" + s[idx-1].lower() + s[idx:].lower()
        
        rs = (s.replace("(", "").replace(")", "").replace("-", "").replace("+", ""))


        local_num = rs[-4:]
        hash_num = "***-***-" + local_num

        if len(rs)==10:
            return(hash_num)
        elif len(rs)==11:
            return("+*-" + hash_num)
        elif len(rs)==12:
            return("+**-" + hash_num)
        elif len(rs)==13:
            return("+***-" + hash_num)
