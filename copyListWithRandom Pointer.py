"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.insertCopyNodes(head)
        self.connectRandomPointers(head)
        return self.getDeepCopy(head)
    # solve in three steps : insert copy nodes in between two nodes
    # connect the random pointers
    # connect the next pointers and return deep copy
    
    def insertCopyNodes(self, head):
        # Make a new copy node in between nodes, the temp will point to head
        # copynode's next will point to temp's next and current temp's next is the copyNode
        # the temp will move 2 steps further, omitting the copy node
        temp = head
        while temp:
            copyNode = Node(temp.val)
            copyNode.next = temp.next
            temp.next = copyNode
            temp = temp.next.next
        
    def connectRandomPointers(self, head):
        # check is copyNode's random exists
        # copyNode's random will be temp.random.next --> this is the copyNode's random 
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next
            
    def getDeepCopy(self, head):
        # make a new dummy node that connects the copy nodes
        # finally return the dummyNode's next 
        temp = head
        dummyNode = Node(-1)
        res = dummyNode
        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return dummyNode.next
            