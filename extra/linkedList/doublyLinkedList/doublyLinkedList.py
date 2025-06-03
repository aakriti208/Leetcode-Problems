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
        
arr = [1, 5, 7, 13, 55, 99]
ll = DoublyLinkedList()
ll.convertToLL(arr)
ll.printLL()
        
    