class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        left, right = [1] * l, [1] * l
        ans = [1] * l

        for i in range(1, l):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(l - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(l):
            ans[i] = left[i] * right[i]

        return ans
