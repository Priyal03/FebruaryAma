from collections import Counter
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], target: int) -> int:
        # Count the frequency of each number in the original array
        originalFreq = Counter(nums)

        def maxGainByConvertingToTarget(source: int) -> int:
            """
            Calculates the maximum number of `source` elements that can be
            converted to `target` in a single subarray operation without reducing
            existing occurrences of `target`.
            """
            maxGain = 0
            currentGain = 0

            for num in nums:
                if num == target:
                    currentGain -= 1  # Avoid overwriting existing target values
                if num == source:
                    currentGain += 1  # Potential to convert this source to target

                if currentGain < 0:
                    currentGain = 0  # Reset streak if it's hurting the result

                maxGain = max(maxGain, currentGain)

            return maxGain

        # Find the best gain from converting any other number to the target
        bestConversionGain = max(maxGainByConvertingToTarget(num) for num in originalFreq)

        # Final answer is original count of target + best possible gain
        return originalFreq[target] + bestConversionGain


        # count = Counter()
        # result = 0

        # for num in nums:

        #     count[num] = max(count[num], count[k]) + 1
        #     print("for num"+str(num))
        #     print(count)


        #     result = max(result, count[num] - count[k])

        # return count[k] + result
