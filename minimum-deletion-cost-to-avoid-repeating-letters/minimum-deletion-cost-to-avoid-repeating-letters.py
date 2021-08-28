class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        n = len(s)
        s_sum = 0
        s_max = 0
        ans = 0
        
        for i in range(0 , n):
          if(s[i] != s[i-1] and i > 0):
            ans += s_sum - s_max
            s_sum = 0
            s_max = 0
            
          s_sum += cost[i]
          s_max = max(s_max , cost[i])
          
        ans += s_sum - s_max
        
        return ans