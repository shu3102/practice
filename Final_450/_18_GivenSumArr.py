class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        temp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if(arr[i] + arr[j] == k):
                    temp += 1
        return temp

