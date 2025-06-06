class Solution:
    def rotateList(self, head, k):
        if head is None or k == 0:
            return head
        
        tail = head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
            
        k = k % count
        if k == 0: return head
        tail.next = head
        diff = count - k
        newLastNode = self.findNthNode(head, diff)
        head = newLastNode.next
        newLastNode.next = None
        return head

    def findNthNode(self, current, k):
        count = 1
        while current:
            if count == k: return current
            count += 1
            current = current.next
        return None