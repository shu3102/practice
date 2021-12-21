

class Solution:    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        s = set()
        p = 0
        for i in range(n):
            p += arr[i]
            if(p == 0):
                return True
            if(p in s):
                return True
            s.add(p)
        return False
