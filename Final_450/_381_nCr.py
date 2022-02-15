
class Solution:
    def fact(self, n):
        i = 1
        for j in range(2, n+1):
            i = i * j
        return i
    
    def nCr(self, n, r):
        # code here
        t = self.fact(n)//(self.fact(n-r)*self.fact(r))
        return int(t%1000000007)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends