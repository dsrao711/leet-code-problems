# User function Template for Python3

class Solution:
    def isSubsetSum(self,n, arr, sum):
        # code here 
        subset = ([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
        
        for i in range(n + 1):
            subset[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j<arr[i-1]:
                    subset[i][j] = subset[i-1][j]
                if j>= arr[i-1]:
                    subset[i][j] = (subset[i-1][j] or 
                                    subset[i - 1][j-arr[i-1]])
    
        return subset[n][sum]
        
    def equalPartition(self, N, arr):
        # code here
        arr_sum = sum(arr)
        
        if(arr_sum % 2 != 0):
            return False
        elif(arr_sum % 2 == 0):
            return self.isSubsetSum(N , arr , arr_sum//2)

#{ 
#  Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends