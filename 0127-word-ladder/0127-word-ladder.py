class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        hashmap = defaultdict(list)
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1 :]
                hashmap[pattern].append(word)

        queue = deque([(beginWord, 1)])  # word, level
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            if word == endWord:
                return level
            visited.add(word)

            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1 :]

                for nei in hashmap[pattern]:
                    if nei not in visited:
                        queue.append((nei, level + 1))

        return 0

# Time: O(N * L²) where N = len(wordList), L = word length.
# Space: O(N * L) for pattern dictionary.