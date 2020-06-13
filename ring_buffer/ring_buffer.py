class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.count = 0

    def append(self, item):
        #if len storage is less than capacity
        #append to list
        if self.count < self.capacity:
            self.storage.append(item)
        #if len storage is equal to capacity
        else:
            #in storage[index] and insert item in its place.
            #at first index =0
            self.storage[self.count % self.capacity] = item
            #increment index by 1 each time you replaced index with new item
        self.count += 1

    def get(self):
        #return storage of items 
        return self.storage