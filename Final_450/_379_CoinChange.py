
class Solution:
    def count(self, S, m, n): 
        # code here 
        t = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i == 0):
                    t[i][j] = 0
                if(j == 0):
                    t[i][j] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if(S[i-1] <= j):
                    t[i][j] = t[i - 1][j] + t[i][j-S[i-1]]
                else:
                    t[i][j] = t[i - 1][j]
        return t[m][n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends