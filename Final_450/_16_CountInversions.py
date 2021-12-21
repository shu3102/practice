# Method 1
def getInvCount(arr, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count

# Method 2 
class Solution:
    def merge(self,arr): 
        # code here\
        temp = 0
        n = len(arr)
        if(n <= 1):
            return arr, temp
        t = n//2
        lsort, ltemp = self.merge(arr[:t])
        rsort, rtemp = self.merge(arr[t:])
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
                temp += nl - i 
                
        while(i < nl):
            l.append(lsort[i])
            i += 1 
        while(j < nr):
            l.append(rsort[j])
            j += 1
        return l, temp + ltemp + rtemp 

    def inversionCount(self, arr, n):
        a, ans = self.merge(arr)
        return ans



        