class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        while temp:
            kthNode = self.findKthNode(temp, k)
            # when the linked list reaches the end or there arent kth node....check if there is any prevNode first
            if kthNode is None:
                if prevNode: prevNode.next = temp
                break
            
            # detach from the linked list and reverse the individual list
            # keep track of nextNode 
            nextNode = kthNode.next
            kthNode.next = None
            self.reverseList(temp)
            
            # if temp == head, i.e., it is the first node in the linked list...the head will be the kth node
            # else, the prevNode's next node will be the kth node of another list
            # store the temp node in a variable called prevNode
            # then out current temp will be the nextNode
            # finally return head of the linked list
            
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp 
            temp = nextNode
        return head
        
    def findKthNode(self, temp, k):
        k -= 1
        while temp and k > 0:
            temp = temp.next
            k -= 1
        return temp
    
    def reverseList(self, head):
        temp, prev = head, None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
            
            
            
            