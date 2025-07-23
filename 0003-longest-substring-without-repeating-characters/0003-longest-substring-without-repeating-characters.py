#for unicode 154,998 chars
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left =0
#         maxlen = 0
#         occur={}

#         for i in range(len(s)):
#             if s[i] in occur:
#                 left = max(left, occur[s[i]]+1)
#             maxlen = max(maxlen, i-left+1)
#             occur[s[i]]=i

#         return maxlen

#for ASCII 256 bit inputs
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