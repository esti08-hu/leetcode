class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res, stack, prev_time = [0] * n, [], 0

        for log in logs:
            id, log_type, time = log.split(":")
            id = int(id)
            time = int(time)

            if log_type == "start":
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        
        return res