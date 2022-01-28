class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        
        for i in range(1,n):
            max_for_i = 0
            for j in range(0 , i):
                if(nums[j] < nums[i]):
                    if(dp[j] > max_for_i):
                        max_for_i = dp[j]
                        
            dp[i] = max_for_i + 1
            
        print(dp)
        
        longest_inc_sub_seq = 1
        for i in range(0 , n):
            if(dp[i] > longest_inc_sub_seq):
                longest_inc_sub_seq = dp[i]
                
        return longest_inc_sub_seq
        