# Every time we decrease count, it’s like canceling one occurrence of the candidate with one occurrence of a different number.

# Since the majority element occurs more than all others combined, it cannot be fully canceled out.

# So at the end, the candidate must be the majority element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num==candidate:
                count += 1
            else:
                count -=1

            # print(str(num) +' hey ' + str(candidate))
            # print('count '+str(count))

        return candidate

# Boyer-Moore is the optimal one (O(N), O(1)) → most interviewers expect you to reach it.