class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        heap = [(-count,char) for char,count in freq.items()]
        heapq.heapify(heap)

        ans=[]

        while heap:
            topCount, topChar = heapq.heappop(heap)
            if not ans or topChar != ans[-1]:
                ans.append(topChar)
                if topCount+1 < 0:
                    heapq.heappush(heap,(topCount+1,topChar))

            else:
                if not heap: # ran out of other lesser chars and have the most occuring in more number, that is invalid.
                    return ''
                secondCount, secondChar = heapq.heappop(heap)
                ans.append(secondChar)
                if secondCount +1 <0:
                    heapq.heappush(heap, (secondCount+1,secondChar))

                heapq.heappush(heap,(topCount,topChar))

        return "".join(ans)

# O(n logk) for heap ops and O(k) for freq