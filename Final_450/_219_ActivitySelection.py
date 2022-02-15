#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        temp = 0
        currtime = 0
        arr1 = [[start[i], end[i]] for i in range(n)]
        arr = sorted(arr1, key = lambda x: x[1])
        #print(arr1)
        #print(arr)
        for i in range(n):
            if(arr[i][0] > currtime):
                temp += 1
                currtime = arr[i][1]
        return temp
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends