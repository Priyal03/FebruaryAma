class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_count, max_letter = 0, ""

        for char, count in freq.items():
            if count > max_count:
                max_count = count
                letter = char

        if max_count > (len(s) + 1) // 2:
            return ""

        ans = [""] * len(s)
        index = 0

        while max_count > 0: # place the most freq character from index 0 to all even places
            ans[index] = letter
            index += 2
            max_count -= 1

        freq[letter] = max_count

        for char, count in freq.items(): # place rest of the chars in any order.
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                count -= 1
                index+=2

        return "".join(ans)


# Time complexity: O(N). We will have to iterate over the entire string once to gather the counts of each character. Then, we we place each character in the answer which costs O(N).

# Space complexity: O(k). The counter used to count the number of occurrences will incur a space complexity of O(k). Again, one could argue that because k <= 26, the space complexity is constant.