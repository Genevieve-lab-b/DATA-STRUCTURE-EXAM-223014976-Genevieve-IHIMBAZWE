class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            return "Circular Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return "Circular Queue is empty"
        elif self.front == self.rear:  # Single element case
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp

    def peek(self):
        if self.is_empty():
            return "Circular Queue is empty"
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            return "Circular Queue is empty"
        elements = []
        i = self.front
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return elements

order_queue = CircularQueue(3)
order_queue.enqueue("Order 1: Cement")
order_queue.enqueue("Order 2: Steel")
order_queue.enqueue("Order 3: Bricks")
print(order_queue.display())
print(order_queue.dequeue())
order_queue.enqueue("Order 4: Sand")
print(order_queue.display())
print(order_queue.is_full()) 
