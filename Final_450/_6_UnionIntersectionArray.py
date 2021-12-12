#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        a = a + b
        return len(set(a))
    
    def doUnion2(a, n, b, m):
        # copy complete array to first array
        for i in b:
            if(i not in a):
                a.append(i)
        
    def doInter(a, n, b, m):
        l = []
        for i in b:
            if(i in a):
                l.append(i)
    

# more approaches using hashing and 
# Sorting 

            
    
