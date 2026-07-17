# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        target, current = head, head

        for _ in range(n):
            current = current.next
        
        if current == None:
            return head.next
        
        current = current.next
        while current:
            target = target.next
            current = current.next
        
        target.next = target.next.next
        return head

