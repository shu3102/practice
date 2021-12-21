
class Solution:
    def factorial(self, N):
        resInt = 1
        resStr = ""
        res = []
        for i in range(1, N+1):
            resInt *= i
        resStr = str(resInt)
        for i in resStr:
            res.append(int(i))
        return res
        