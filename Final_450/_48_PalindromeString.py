#User function Template for python3
class Solution:
	def isPalindrome(self, S):
	    return 1 if S == "".join(S[::-1]) else 0
	    
