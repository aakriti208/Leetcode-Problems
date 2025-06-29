class queueUsingStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
        def enqueue(self, x):
            self.in_stack.append(x)
            
        def dequeue(self):
            if self.empty():
                return "Queue is empty"
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()
        
        def peek(self):
            if self.empty():
                return "Queue is empty"
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]
        
        def empty(self):
            return not self.in_stack and not self.out_stack
    
    