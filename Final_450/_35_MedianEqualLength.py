
class Solution: 
    def find_median(self, v):
        # Code here 
        v.sort()
        t = len(v)
        if(t % 2 == 1): 
            return v[t//2]
        else:
    	    return (v[t//2] + v[t//2 - 1])//2

