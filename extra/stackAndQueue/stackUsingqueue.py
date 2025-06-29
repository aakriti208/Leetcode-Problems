class Stack:
    def __init__(self):
        # have two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        # Push x first in empty queue
        self.q2.append(x)
        
        # transfer all elements from q1 to q2
        while(self.q1):
            self.q2.append(self.q1.popleft())
            
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        if self.empty():
            return "Stack is empty"
        return self.q1.popLeft()    # Top of stack in front of q1
    
    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.q1[0]    # Top of stack is front of q1
    
    def empty(self):
        return len(self.q1) == 0
    
        