
from collections import deque

class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycleUtil(self , adj , s , vis):
        vis[s] = 1
        q = deque()
        q.append([s , -1])
        while(q):
            node , parent = q.popleft()
            
            for i in adj[node]:
                if(vis[i] == 0):
                    q.append( [i , node])
                    vis[i] = 1
                elif(i != parent):
                    return True
        return False
        
        
	def isCycle(self, V, adj):
		#Code here
		vis = [0]*V
		for i in range(V):
		    if(vis[i] == 0):
		        if(self.isCycleUtil(adj , i , vis) == True):
		            return True
		return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends