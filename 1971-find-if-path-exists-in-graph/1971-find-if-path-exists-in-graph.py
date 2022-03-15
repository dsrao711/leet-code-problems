class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # create adj list 
        d = defaultdict(set)
        for u , v in edges : 
            d[u].add(v)
            d[v].add(u)
            
        print(d)
        
        # bfs
        def bfs(s,d,adjlist):
            
            q = deque()
            vis = set()
            q.append(s)

            while q:
                curr = q.popleft()
                if(curr == d):
                    return True
                vis.add(curr)
                for i in adjlist[curr]:
                    if(i not in vis):
                        vis.add(i)
                        q.append(i)
                        
            return False
        
        return bfs(source , destination, d)
                
                        
        
                
    
        
        