class QueueFromTwoStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, val):
        self.enqueue_stack.append(val)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

def process_operations(operations):
    queue = QueueFromTwoStacks()
    min_stack = MinStack()
    outputs = []

    for op in operations:
        if op[0] == "enqueue":
            queue.enqueue(op[1])
        elif op[0] == "dequeue":
            outputs.append(queue.dequeue())
        elif op[0] == "mpush":
            min_stack.push(op[1])
        elif op[0] == "mpop":
            outputs.append(min_stack.pop())
        elif op[0] == "mtop":
            outputs.append(min_stack.top())
        elif op[0] == "mmin":
            outputs.append(min_stack.min())

    return outputs