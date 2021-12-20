print()
#User function Template for python3

class Solution:
    #def merge(self,arr, l, m, r): 
    def merge(self,arr): 
        # code here\
        n = len(arr)
        if(n <= 1):
            return arr
        t = n//2
        lsort = self.merge(arr[:t])
        rsort = self.merge(arr[t:])
        nl = len(lsort)
        nr = len(rsort)
        
        l = []
        i = j = 0
        while(i < nl and j < nr):
            if(lsort[i] < rsort[j]):
                l.append(lsort[i])
                i += 1
            else:
                l.append(rsort[j])
                j += 1
            
        while(i < nl):
            l.append(lsort[i])
            i += 1 
        while(j < nr):
            l.append(rsort[j])
            j += 1
        return l
 
    def mergeSort(self,arr, l, r):
        #code here
        llt = self.merge(arr)
        #print(llt)
        for i in range(r + 1):
            arr[i] = llt[i] 
        arr = llt
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
