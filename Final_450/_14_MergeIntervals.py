#Trying
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        Mx = max(intervals)
        Mx = max(Mx)
        
        arr = [0]*(Mx+2)
        print(intervals)
        print(Mx)
        special = 0
        for i in intervals:
            if(i[0]==0):
                k = 1
                special = 1
            else:
                k = 1
            fg = 1
            for j in range(i[0], i[1]+1):
                if(fg and arr[j] > 1):
                    if(special):
                        k = j - 1
                    else:
                        k = j
                    fg = 0
                arr[j] = k
                k += 1
        print(arr)
        op = []
        
        i = 0
        while(i < Mx):
            if(arr[i] == 1):
                t = []
                if(special):
                    i = 0
                t.append(i)
                i += 1
                loop = 0
                while(arr[i] > 1):
                    i = i + 1
                    loop = 1
                t.append(i-1)
                op.append(t)
                if(loop):
                    i -= 1
                    loop = 0
            i += 1
        print(op)
        return op
            
            