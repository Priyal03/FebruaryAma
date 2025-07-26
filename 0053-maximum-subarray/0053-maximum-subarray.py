class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current=nums[0]
        maxSubArray=nums[0]

        for i in range(1,len(nums)):

            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current = max(nums[i], current+nums[i])

            maxSubArray = max(maxSubArray, current)

        return maxSubArray

# Time complexity: O(N), where N is the length of nums.

# We iterate through every element of nums exactly once.

# Space complexity: O(1)

# No matter how long the input is, we are only ever using 2 variables: currentSubarray and maxSubarray.
