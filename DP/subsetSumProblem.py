"""
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
"""




    
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
        
        return t[N][sum]
                    
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)