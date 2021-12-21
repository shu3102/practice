

"""
Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination: 
The two parts are {1, 5, 5} and {11}.
"""




class Solution:
    def issubsetsum(self, N, arr, S):
        t = [[0 for j in range(S+1)] for i in range(N + 1)]
        for i in range(N+1):
            for j in range(S+1):
                if(i == 0):
                    t[i][j] = False
                if(j == 0):
                    t[i][j] = True
        for i in range(1, N+1):
            for j in range(1, S+1):
                if(arr[i-1] <= j):
                    t[i][j] = t[i-1][j - arr[i-1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[N][S]
                    
        
    def equalPartition(self, N, arr):
        # code here
        su = sum(arr)
        if(su % 2 == 1):
            return 0
        else:
            v = self.issubsetsum(N, arr, su//2)
            if(v == True):
                return 1
            else:
                return 0
            

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