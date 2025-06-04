# cook your dish here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def from_array(self, values):
        if not values:
            return
        self.head = Node(values[0])
        curr = self.head
        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")
     
    def seggregateEvenOdd(self):
        if self.head is None or self.head.next is None:
            return self.head
        zeroHead = Node(-1)
        zero = zeroHead
        oneHead = Node(-1)
        one = oneHead
        twoHead = Node(-1)
        two = twoHead
        current = self.head
        while current:
            if current.data == 0:
                zero.next = current
                zero = current
            elif current.data == 1:
                one.next = current
                one = current
            else:
                two.next = current
                two = current
            current = current.next
        
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next if twoHead.next else None
        two.next = None
        
        self.head = zeroHead.next
        return self.head
            
            
ll = LinkedList()
ll.from_array([0,2,1,1,0,0,1])
print("Original list:")
ll.print_list()
ll.seggregateEvenOdd()
print("Segregated list:")
ll.print_list()



def seggregateEvenOdd(self):
    # check if the head or next of head is present
        if self.head is None or self.head.next is None:
            return self.head
        # make three dummy nodes for 0, 1 and 2 and initialize their head as zeroHead
        zeroHead = Node(-1)
        zero = zeroHead
        oneHead = Node(-1)
        one = oneHead
        twoHead = Node(-1)
        two = twoHead
        # the current always points to the head, then loop through each nodes
        current = self.head
        while current:
            # if the current node's data is 0, the zero's next pointer will point to the current and the zero node will point to the current node
            # same for 1 and 2, then the current will also point to current.next
            if current.data == 0:
                zero.next = current
                zero = current
            elif current.data == 1:
                one.next = current
                one = current
            else:
                two.next = current
                two = current
            current = current.next
        # connect the three lists
        # now if we have the one's list, 0's next will point to the one's list. same for one and two
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next if twoHead.next else None
        two.next = None
        
        # now the original head will point to the start of the new sorted list
        self.head = zeroHead.next
        return self.head
