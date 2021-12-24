class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        # Left pointer and right pointer for defining the window
        l = 0 
        r = len(cardPoints) - k
        curr_sum = sum(cardPoints[r:])
        max_sum = curr_sum
        
        while(r < len(cardPoints)):
            curr_sum += (cardPoints[l] - cardPoints[r])
            max_sum = max(curr_sum , max_sum)
            l += 1
            r += 1
        
        return max_sum
        
        