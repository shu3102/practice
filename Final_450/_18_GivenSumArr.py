class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        temp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if(arr[i] + arr[j] == k):
                    temp += 1
        return temp
    
    def getPairsCount____(self, arr, n, k):
        # code here
        d = {}
        c = 0
        for i in range(n):
            if(k - arr[i] in d):
                c += d[k - arr[i]]
            if(arr[i] in d):
                d[arr[i]] += 1
            if(arr[i] not in d):
                d[arr[i]] = 1
        return c
                
    # third approach using array and counting index

