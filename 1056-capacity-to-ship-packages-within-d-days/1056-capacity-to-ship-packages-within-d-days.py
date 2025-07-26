class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(currentShipCapacity):

            daysNeeded = 1
            currentLoad = 0
            for i in range(len(weights)):

                currentLoad += weights[i]
                if currentLoad > currentShipCapacity:

                    currentLoad = weights[i]
                    daysNeeded += 1

            return daysNeeded <= days


# binary search for the answer, as answer could be in range of [max(inputs), sum(inputs)]
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left

# Time complexity: O(n⋅log(500⋅n))=O(n⋅log(n))

# It takes O(n) time to iterate through weights to compute maxLoad and totalLoad.

# In the binary search algorithm, we divide our range by half every time. So for a range of length R, it performs O(log(R)) operations. In our case, the range is from maxLoad to totalLoad. As mentioned in the problem constraints, maxLoad can be 500, so the total load can be n * 500. So, in the worst case, the size of the range would be (n - 1) * 500 which would require O(log(500n−500))=O(log(n)) operations using a binary search algorithm.

# To see if we can deliver the packages in the required number of days with a specific capacity, we iterate through the weights array to see if the current capacity allows us to carry the all the packages in days days, which needs O(n) time.

# So it would take O(n⋅log(n)) time in total.

# Space complexity: O(1)

# We are only defining a few integer variables.