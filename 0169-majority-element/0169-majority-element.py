class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = Counter(nums)
        half = len(nums) / 2

        for digit, count in freq.items():
            
            if count > half:
                return digit

        return -1

# O(N) and O(N)