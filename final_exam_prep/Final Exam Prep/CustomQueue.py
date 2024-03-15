class CustomQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def print_contents(self):
        for i in range(len(self.queue) - 1, -1, -1):
            print(self.queue[i])
