class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap={}

        for index, val in enumerate(nums):
            
            complement = target-val

            if complement in hashmap:
                return [hashmap[complement],index]

            hashmap[val]=index

        return []