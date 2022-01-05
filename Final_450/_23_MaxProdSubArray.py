# User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
    def maxProduct(self, arr, n):
        result = arr[0]

        for i in range(n):
            mul = arr[i]
            for j in range(i + 1, n):
                result = max(result, mul)
                mul *= arr[j]
	        result = max(result, mul) 
        return result




        







