from linkedList import singlyLinkedList

def create_linked_list(values):
    if not values:
        return None
    
    head = singlyLinkedList(values[0])
    current = head
    
    for value in values[1:]:
        current.next = singlyLinkedList(value)
        current = current.next
        
    return head
    
    

## Traversing the linked list
def traverse(head):
    # start from the head
    current = head

    # loop through the list while current is not None:
    while current:
        
        # Access the data
        print(current.value, end=" --> ")
        
        # Update the current pointer current = current.next
        current = current.next
    print("None")



    
        