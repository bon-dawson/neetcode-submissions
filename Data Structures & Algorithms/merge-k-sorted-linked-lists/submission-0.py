# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mn_heap = []
        counter = 0
        for l in lists:
            heapq.heappush(mn_heap, (l.val, counter, l))
            counter += 1

        dummy = ListNode()
        cur = dummy
        while mn_heap:
            val, _, min_node = heapq.heappop(mn_heap)

            cur.next = min_node
            cur = cur.next

            next_node = min_node.next
            if next_node:
                heapq.heappush(mn_heap, (next_node.val, counter, next_node))
                counter += 1

        return dummy.next