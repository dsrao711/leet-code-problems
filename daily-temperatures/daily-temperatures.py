class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        op = [0]*n
        stack = []
        
        for curr_day , curr_temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < curr_temp :
                prev_day = stack.pop()
                op[prev_day] = curr_day - prev_day
            stack.append(curr_day)
            
        return op
            