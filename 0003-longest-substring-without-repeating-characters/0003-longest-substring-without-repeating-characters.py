class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        occur = [None]*128

        for curr in range(len(s)):

            past_occurrence = occur[ord(s[curr])]
            
            if past_occurrence is not None: #if you find again.
            
                left = max(past_occurrence + 1, left)#update the left bound value.

            maxlen = max(maxlen, curr - left + 1)

            occur[ord(s[curr])] = curr #save everytime at curr index.

        return maxlen
