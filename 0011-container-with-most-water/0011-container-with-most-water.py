class Solution:
    def maxArea(self, height: List[int]) -> int:
        startLine=0
        endLine = len(height)-1
        maxWater = 0

        while startLine < endLine:
            currentWater = min(height[endLine],height[startLine])*(endLine-startLine)
            maxWater=max(maxWater,currentWater)
            if height[endLine]<height[startLine]:
                endLine-=1
            else:
                startLine+=1

        return maxWater

# Time complexity: O(n). Single pass.

# Space complexity: O(1). Constant space is used.