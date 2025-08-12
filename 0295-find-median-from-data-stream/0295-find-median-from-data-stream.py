class MedianFinder:

    def __init__(self):
        self.nums=[]
        self.length=0

    def addNum(self, value: int) -> None:
        self.length+=1
        if not self.nums:
            self.nums.append(value)
        else:
            left_index = bisect.bisect_left(self.nums, value)
            self.nums.insert(left_index, value)

    def findMedian(self) -> float:
        half = self.length//2
        if self.length & 1 :
            return float(self.nums[half])
        else:
            return (self.nums[half]+self.nums[half-1])/2

# O(N) due to list insertion. and O(N) for nums

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()