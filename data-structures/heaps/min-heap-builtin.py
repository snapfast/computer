import heapq


class MinHeap():
    """docstring for MinHeap"""

    def __init__(self):
        super(MinHeap, self).__init__()
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        heapq.heappop(self.heap)

    def find_min(self):
        return heapq.nsmallest(3, self.heap)

    def delete_min(self):
        pass

    def replace(self):
        # pop, push then rebalancing
        heapq.heapreplace()

    def heapify(self):
        pass


mh = MinHeap()
mh.insert(4)
print(mh.heap, mh.find_min())
mh.insert(5)
print(mh.heap, mh.find_min())
mh.insert(63)
mh.insert(45)
mh.insert(22)
print(mh.heap, mh.find_min())
