class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        queue = deque([])
        translate = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i not in translate:
                queue.append(i)
            elif len(queue) == 0 or translate[i] != queue[-1]:
                return False
            else:
                queue.pop()
        
        return len(queue) == 0