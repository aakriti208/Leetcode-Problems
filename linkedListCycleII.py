class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # detect a cycle using tortoise and hare solution
            if slow == fast:
                break
        else: return None
        
        # finding the starting point
        # take the pointer slow to the head of the linked list to check where they collide
        # move slow and fast by one steps as long as they dont collide
        # the point they collide or meet is the starting point...it could return either slow or fast any
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
