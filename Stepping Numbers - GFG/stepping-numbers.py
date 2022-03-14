#User function Template for python3

from collections import deque
class Solution:
    def bfs(self , num , n , m):
        count = 0
        q = deque()
        q.append(num)
        while(q):
            stepNum = q.popleft()
            if(stepNum >= n and stepNum <= m):
                count += 1
            if(stepNum <= 0 or stepNum > m):
                continue
            l = stepNum % 10 
            stepNumA = stepNum * 10 + (l - 1)
            stepNumB = stepNum * 10 + (l + 1)
            if(l == 0):
                q.append(stepNumB)
            elif(l == 9):
                q.append(stepNumA)
            else:
                q.append(stepNumA)
                q.append(stepNumB)
            
        return count 
        
    def steppingNumbers(self, n, m):
        # code here
        count = 0
        for i in range(10):
            count += self.bfs(i , n , m)
            
        return count
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N, M = map(int, input().split())
        ans = ob.steppingNumbers(N, M);
        print(ans)




# } Driver Code Ends