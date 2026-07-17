# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        while True:
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            current.val, carry = current.val % 10, current.val // 10
            if l1 or l2 or carry:
                current.next = ListNode(val=carry)
                current = current.next
                continue
            break
        return result
        