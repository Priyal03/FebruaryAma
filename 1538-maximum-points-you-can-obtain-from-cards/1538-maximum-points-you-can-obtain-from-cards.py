class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        def getMinimumScore(length):
            
            currentSum = sum(cardPoints[:length])
            result = currentSum
            
            for i in range(length, len(cardPoints)):
                
                currentSum+=cardPoints[i] - cardPoints[i-length]
                result=min(result, currentSum)
            
            return result

        window = len(cardPoints) - k

        minimumSum = getMinimumScore(window) 

        return sum(cardPoints) - minimumSum



# timeComplexity = O(n)
# SpaceComplexity = O(1)
