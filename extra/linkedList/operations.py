from linkedList import singlyLinkedList

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



    
        