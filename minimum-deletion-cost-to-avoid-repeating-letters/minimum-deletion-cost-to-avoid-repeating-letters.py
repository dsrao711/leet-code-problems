class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        total_cost = 0
        prev_index = 0
        i = 1
        n = len(s)
        while(i < n):
          if(s[prev_index] == s[i]):
            total_cost += min(cost[prev_index] , cost[i])
            
            if(cost[prev_index] < cost[i]):
              prev_index = i
              
          else:
            prev_index = i
          
          i += 1
          
        return total_cost