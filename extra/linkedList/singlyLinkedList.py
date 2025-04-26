class singlyLinkedList:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        


node1 = singlyLinkedList("4")
node2 = singlyLinkedList("5")
node3 = singlyLinkedList("8")
node1.next = node2
node2.next = node3

currentNode = node1
while currentNode:
    print(currentNode.value, end="-->")
    if currentNode.next == None:
        print("None")
        break
    currentNode = currentNode.next
    