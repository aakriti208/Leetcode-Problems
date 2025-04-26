from linkedList import singlyLinkedList
from operations import traverse

if __name__ == "__main__":
    node1 = singlyLinkedList("2")
    node2 = singlyLinkedList("5")
    node3 = singlyLinkedList("10")
    node1.next = node2
    node2.next = node3

    traverse(node1)
        