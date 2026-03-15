# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None and head.next is None:
            return True
        
        # finding the middle node
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        newHead = self.reverse(slow.next)

        # compare the values of the two halves
        first = head
        second = newHead
        while second:
            if first.val != second.val:
                self.reverse(newHead)
                return False
            first = first.next
            second = second.next
        self.reverse(newHead)
        return True



   


        