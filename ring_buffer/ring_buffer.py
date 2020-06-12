class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        #add to list
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage[self.index] = item
            self.index += 1
            if self.index == self.capacity:
                self.index = 0
            
        #if len > capacity then self.storage.append()
        # if len < capacity

    def get(self):
        return self.storage