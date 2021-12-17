# Solution if elements not repeted more than twice 
class Solution:
    def findDuplicate(self, nums):
        arrSum = sum(nums)
        n = len(nums)
        n -= 1
        #print(n)
        t = int(n*(n + 1)/2)
        #print(t)
        #print(arrSum)
        return arrSum - t

    def findDuplicate_forRepeted(self, nums):
        n = len(nums)
        arr = [0]*(n - 1)
        for i in nums:
            arr[i - 1] += 1
            if(arr[i - 1] > 1):
                return i
        
        