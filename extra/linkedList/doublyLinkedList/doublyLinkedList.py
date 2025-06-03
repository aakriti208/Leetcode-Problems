class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def convertToLL(self, values):
        self.head = Node(values[0], None, None)
        prev = self.head
        
        for value in values[1:]:
            temp = Node(value, None, None)
            prev.next = temp
            prev = temp
            
        return self.head
        
    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data, end = " ")
            curr = curr.next
        print("None")
        
    def deleteHead(self):
        if self.head is None:
            return 
        #if only one node, set the head to none and delete
        if self.head.next is None:
            self.head = None
        else:
            # if more than one node, set head to the second node
            # remove the back link from the new head to the old head that cuts off the old head from the list
            self.head = self.head.next
            self.head.prev = None
            
    def deleteTail(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
        else:
            tail = self.head
            # go till the end of the list
            while tail.next is not None:
                tail = tail.next
            # tail.prev points to [55]...so [55].next = None will be done and [99] will be unlinked and discarded 
            tail.prev.next = None            
              
    def deleteKthElement(self, k):
        if self.head is None or k <= 0:
            return
        
        if k == 1:
            self.deleteHead()
            return
        
        count = 0
        current = self.head
        # go to the kth node
        while current and count < k:
            current = current.next
            count += 1
        # if k > length of the list, do nothing
        if current is None: 
            return 
        # delete the tail
        if current.next is None:
            self.deleteTail()
            return
        # delete the middle node
        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        #optional only for cleanup
        current.prev = None
        current.next= None
        
        
        
arr = [1, 5, 7, 13, 55, 99]
ll = DoublyLinkedList()
ll.convertToLL(arr)
ll.deleteHead()
ll.deleteTail()
ll.deleteKthElement(2)
ll.printLL()
        
    