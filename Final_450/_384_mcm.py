import sys
t = [[ -1 for j in range(101)] for i in range(101)]

 #print(t)
def solve(arr, i, j):
        if(i == j):
            return 0
        if(t[i][j] != -1):
            return t[i][j]
        mn = sys.maxsize
        temp_ans = 0
        for k in range(i, j):
            t[i][j] = min(mn, solve(arr, i, k) + solve(arr, k + 1, j) + arr[i-1]*arr[k]*arr[j])
            
        return t[i][j]


class Solution:
    
    def matrixMultiplication(self, N, arr):
        # code here
        return solve(arr, 1, len(arr)-1)
        
if __name__ == '__main__':
    ob = Solution()
    print(ob.matrixMultiplication(5, [40, 20, 30, 10, 30]))
# } Driver Code Ends