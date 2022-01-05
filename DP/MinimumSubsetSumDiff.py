#User function Template for python3
class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        t = [[0 for j in range(sum + 1)] for i in range(N + 1)]
        # Initialization 
        for i in range(N + 1):
            for j in range(sum + 1):
                if(i == 0):
                    t[i][j] = False
                if(j == 0):
                    t[i][j] = True
        
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if(arr[i - 1] <= j):
                    t[i][j] = t[i-1][j-arr[i - 1]] or t[i-1][j]
                    #DP[i][j] = DP[i-1][j] OR DP[i-1][j-A[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[N]
                    
                    
    def minDifference(self, arr, n):
		# code here
	    s = sum(arr)
	    myarr = self.isSubsetSum(n, arr, s//2)
	    mn = s
	    for i in range(1, len(myarr)):
		    if(myarr[i] == True):
		        t = s - 2 * i
		        if(t < mn):
		            mn = t
	    return mn
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends