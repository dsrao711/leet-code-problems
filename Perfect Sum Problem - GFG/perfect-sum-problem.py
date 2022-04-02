#User function Template for python3
class Solution:
	def perfectSum(self, a, n, sum):
		# code here
		new_arr = [i for i in arr if i!=0]
	    zero_cnt = len(arr) - len(new_arr)
	    
		tab = [[0] * (sum + 1) for i in range(n + 1)]
        tab[0][0] = 1
        for i in range(1, sum + 1):
            tab[0][i] = 0
         
        for i in range(1, n+1):
            for j in range(sum + 1):
                if a[i-1] <= j:
                    tab[i][j] = (tab[i-1][j] + tab[i-1][j-a[i-1]]) %1000000007
                else:
                    tab[i][j] = (tab[i-1][j]) % 1000000007
                    
        return (tab[n][sum]) %1000000007 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends