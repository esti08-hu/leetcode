class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if line[i:i+2] == '/*':
                        in_block = True
                        i += 1
                    elif line[i:i+2] == '//':
                        break
                    else:
                        new_line.append(line[i])
                else:
                    if line[i:i+2] == '*/':
                        in_block = False
                        i += 1
                i += 1
            if new_line and not in_block:
                res.append("".join(new_line))
                new_line = []
        
        return res