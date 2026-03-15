# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is None:
            return None
        t1 = headA
        t2 = headB
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
            if t1 == t2:
                return t1
            if t1 is None:
                t1 = headB
            elif t2 is None:
                t2 = headA
        return t1


# if headA and headB does not exist, return None
# there will be one pointer pointing to each headA and headB
# as long as they are not pointing to the same lists, go through each node
# at the point, where t1 and t2 meet, they intersect so return t1
# but if t1 reaches the end, it will again point to the head of headB....that is list 2
# same with t2
# in the end, return t1