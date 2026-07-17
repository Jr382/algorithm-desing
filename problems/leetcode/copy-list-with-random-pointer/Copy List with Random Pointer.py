"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        maps, copied, current = {}, Node(0), head
        c_current = copied
        while current:
            c_current.next = Node(current.val)
            dic[current] = c_current.next
            current = current.next
            c_current = c_current.next
        
        current = head
        while current:
            if current.random:
                dic[current].random = dic[current.random]
            current = current.next

        return copied.next

