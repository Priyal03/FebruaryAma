class Solution:
    def rob(self, nums: List[int]) -> int:

        secondLastHouse = 0
        lastHouse = nums[0]
        totalRobbery = nums[0]

        for i in range(1, len(nums)):

            totalRobbery = max(nums[i] + secondLastHouse, lastHouse)

            secondLastHouse = lastHouse
            lastHouse = totalRobbery

        return totalRobbery


# slicing the substring every time is more costlier than using a range from 1 to n.
# O(n) and O(1)
