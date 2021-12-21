class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i = j = k = 0
        ans = []
        while(i < n1 and j < n2 and k < n3):
            if(A[i] == B[j]):
                #
                while(k < n3 and C[k] <= A[i]):
                    if(A[i] == C[k]):
                        if(A[i] not in ans):
                            ans.append(A[i])
                    k += 1
            if(A[i] < B[j]):
                i += 1
            else:
                j += 1
        return ans


        