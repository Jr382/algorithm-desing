# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return None
        
        current, swapped = head.next, ListNode(next=head)
        current_head = swapped
        
        while current:
            next_node = current.next
            current.next, current_head.next.next = current_head.next, current.next
            current_head.next, current_head = current, current_head.next
            
            if not next_node:
                break
            current = next_node.next

        return swapped.next
            