class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            idx = s.index("@")
            return s[0].lower() + "*****" + s[idx-1:].lower()
        
        rs = (s.replace("(", "").replace(")", "").replace("-", "").replace("+", "").replace(" ", ""))


        local_num = rs[-4:]
        masked_num = "***-***-" + local_num

        if len(rs)==10:
            return(masked_num)
        elif len(rs)==11:
            return("+*-" + masked_num)
        elif len(rs)==12:
            return("+**-" + masked_num)
        elif len(rs)==13:
            return("+***-" + masked_num)
