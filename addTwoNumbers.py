class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            value = v1 + v2 + carry
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            
            #update pointer
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            
            
        
# make a dummy node to store the new node of sum
# the current pointer will point to the dummy node
# we need to maintain a carry, which will be initialized to 0
# while the list l1 and l2 are not empty or carry is also not empty (8+7=15), we might have a number like this
# value 1 is gonna be value of list 1 if present else will be 0, same for value 2
# for the new digits, we add v1, v2 and carry 
# the carry will be remainder of value and value will be the mod of the value
# now that we have the new digit, we can insert it in our list. we're gonna insert a new listnode with the value that we just computed
# finally we upate all the pointers
 # we're gonna return dummy.next, that is the list that we just created 
 