from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = Counter(nums)#take count of each digit.
        
        heap=[]#create heap to maintain the max element at the top
        for digit, count in occurrences.items():
            heapq.heappush(heap, (-count, digit))#heapify each element.

        res=[]
        #traverse until k elements
        for _ in range(k):
            if heap:
                pair = heappop(heap)#manage heapify after each pop operation
                res.append(pair[1])
            
        return res