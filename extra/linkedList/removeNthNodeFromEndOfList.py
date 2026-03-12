# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0, head)
#         left = dummy
#         right = head
#         while n > 0 and right:
#             right = right.next
#             n -= 1
#         while right != None:
#             left = left.next
#             right = right.next
#         # delete node
#         left.next = left.next.next
#         return dummy.next
    
    
    
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        dummy.next = head
        slow, fast = dummy, dummy
        # initialize both slow and fast pointers to dummy node
        
        for _ in range(n+1):
            fast = fast.next
        # fast will be n+1 steps ahead of slow. Slow will land 1 step before the target
        while fast:
            slow = slow.next
            fast = fast.next
        # slow is now at the nth node from the end
        
        slow.next = slow.next.next      # delete the target node
        return dummy.next
            