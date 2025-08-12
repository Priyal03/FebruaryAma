class MedianFinder:

    def __init__(self):
        self.left = []  # max_heap
        self.right = []  # min_heap

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.left, -num)

        # maintain order
        if self.left and self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        # maintain sizes
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        else:
            return (-self.left[0] + self.right[0]) / 2


# TC log(n) for heap insertion and O(1) for findMedian method and SC O(n) for two heaps

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
