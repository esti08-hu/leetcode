class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dup_files = defaultdict(list)
        answer =[]
        for s in paths:
            all_name = s.split(" ")

            for i in range(1, len(all_name)):
                file_name = all_name[i].split("(")
                dup_files[file_name[1]].append(all_name[0]+"/"+ file_name[0])

        for key in dup_files:
            if len(dup_files[key]) > 1:
                answer.append(dup_files[key])
        return answer
