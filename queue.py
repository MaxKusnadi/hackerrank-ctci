class MyQueue(object):
    def __init__(self):
        self.main_stack = list()
        self.main_queue = list()
        
    
    def peek(self):
        if not self.main_queue:
            while self.main_stack:
                self.main_queue.append(self.main_stack.pop())
        val = self.main_queue.pop()
        self.main_queue.append(val)
        return val
        
    def pop(self):
        if not self.main_queue:
            while self.main_stack:
                self.main_queue.append(self.main_stack.pop())
        return self.main_queue.pop()
        
    def put(self, value):
        self.main_stack.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
