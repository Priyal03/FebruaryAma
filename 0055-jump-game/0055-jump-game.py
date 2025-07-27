class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # jumpCounting the jump summation from start to end.
        jumpCount=0 
        
        for i in range(len(nums)):
            
            # exit whenever jumpCount becomes lesser than index value.
            if jumpCount<i:
                return False  
            
            # at max, jumpCount could be value of arr[i] and how far we already are from index 0 which is i. 
            currentJump=(i+nums[i]) 
            if currentJump>jumpCount:
                jumpCount=currentJump
            
        return True 