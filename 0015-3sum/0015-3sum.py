class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        seen ={}
        dups = set()
        res=set()

        for i, val1 in enumerate(nums):
            
            if val1 not in dups:
                dups.add(val1)

                for j, val2 in enumerate(nums[i+1:]):

                    complement = -val2-val1

                    if complement in seen and seen[complement]==i:

                        res.add(tuple(sorted((val1,val2,complement))))

                    seen[val2]=i # mark val2 visited for val1 

        return [list(x) for x in res]


# O(n^2) and O(n) because of map