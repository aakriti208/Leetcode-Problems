# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        slow = fast = head
        fast = fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        return head
    

# for deleting the middle node, if we reach the node right before the middle node, it'll be easier to delete the middle node
# initially, the fast will move one step but the slow pointer will be one step back....then we find the middle node
# after that, the next pointer of slow will point to the next of next
