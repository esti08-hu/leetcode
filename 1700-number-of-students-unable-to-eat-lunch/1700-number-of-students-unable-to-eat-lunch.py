class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students
        stack = sandwiches

        count = 0
        while count < len(queue):
            if queue[0] == stack[0]:
                queue.pop(0)
                stack.pop(0)
                count = 0  
            else:
                queue.append(queue.pop(0))
                count += 1  

        return len(queue)