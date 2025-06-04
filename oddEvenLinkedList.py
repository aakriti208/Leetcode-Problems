# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
            
        odd.next = even_head
        return head
            
# check is head or head.next is none
# initialize odd node to head, and even node will be the next node to the head
# initialize an even_head that can be used later to join the odd and even node
# Go till the end while even is present and even.next is not none (if even is there odd will also be there)
# now odd's next will be two steps further and so will even's next
# lastly, connect odd'd next to the even_head and return the head