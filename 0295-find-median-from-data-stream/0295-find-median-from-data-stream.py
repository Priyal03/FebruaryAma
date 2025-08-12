class MedianFinder:

    def __init__(self):
        self.nums=[]

    def addNum(self, value: int) -> None:
        if not self.nums:
            self.nums.append(value)
        else:
            left_index = bisect.bisect_left(self.nums, value)
            self.nums.insert(left_index, value)

    def findMedian(self) -> float:
        size = len(self.nums)
        if size & 1 :
            return float(self.nums[size//2])
        else:
            return (self.nums[size//2]+self.nums[size//2-1])/2

# O(N) due to list insertion. and O(N) for nums

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()