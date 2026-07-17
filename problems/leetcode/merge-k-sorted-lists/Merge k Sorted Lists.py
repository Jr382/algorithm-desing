# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = [Node(node) for node in lists if node != None]
        merged = ListNode()
        current = merged
        heapq.heapify(heap)

        while heap:
            smallest = heapq.heappop(heap)
            current.next = smallest.listNode
            if smallest.next:
                heapq.heappush(heap, Node(smallest.next))
            current = current.next
        


        return merged.next

class Node:
    def __init__(self, listNode):
        self.listNode = listNode
        self.val = listNode.val
        self.next = listNode.next
    
    def __lt__(self, other):
        return self.val < other.val