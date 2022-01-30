#User function Template for python3
class Solution:

	def matchPairs(self,nuts, bolts, n):
		# code here
		order = '!#$%&*@^~'

        nut_hash = {}
        for i in range(0 , len(nuts)):
            nut_hash[nuts[i]] = i
            
        j = 0
        for i in range(len(order)):  # O(9) -> O(1)
            if order[i] in nut_hash:  # Average Case - O(1), Worst Case - O(n)
                nuts[j] = order[i]
                bolts[j] = order[i]
                j += 1
		       
		
		   
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends