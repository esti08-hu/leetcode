class Solution:
    def interpret(self, command: str) -> str:
        res =""
        c1= "()"
        c2="(al)"
        c=""
        for s in command:
            if s=="G":
                res+=s
            else:
                c+=s
                if(c==c1):
                    res+='o'
                    c=""
                elif(c==c2):
                    res+="al"
                    c=""
        return res
