# Topic 2: Implement Queue and Circular Queue

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue is full!")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        print("Queue is empty!")
        return None

    def display(self):
        print("Queue:", self.queue)


class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty!")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def display(self):
        print("Circular Queue:", self.queue)


# Example Usage
q = Queue(5)
q.enqueue("Task 1")
q.enqueue("Task 2")
q.display()
q.dequeue()
q.display()

cq = CircularQueue(5)
cq.enqueue("Resource A")
cq.enqueue("Resource B")
cq.display()
cq.dequeue()
cq.display()
