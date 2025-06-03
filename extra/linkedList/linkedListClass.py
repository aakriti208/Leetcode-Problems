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
        #first value becomes the head node
        self.head = Node(values[0])
        # mover is used to traverse and build the list and starts at head
        mover = self.head
        # loop through the array
        # create a new node 'temp'
        # link mover.next to the temp value-this attaches new node to the list
        # move 'mover' to the new node so we can add next node after this
        for value in values[1:]:
            temp = Node(value)
            mover.next = temp
            mover = temp
            
        #start from the head and print each node's data
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " --> ")
            temp = temp.next
        print("None")
        
        
arr = [1,2,4,8,10,12]
ll = LinkedList()
ll.from_array(arr)
ll.print_list()