# time complexity of reversing an array is O(n)
# space complexity is 

a = [1, 2, 3, 4, 5]
# Method 1
# python inbuild function
a.reverse()
print(a)



a = [1, 2, 3, 4, 5]
# Method 2
# swap the first element with last 
i = 0
j = len(a) - 1
while(i < j):
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1
print(a)
# O(n)



a = [1, 2, 3, 4, 5]
# Method 3
# special method in python
# list slicing method 
b = a[::-1]
print(b)


# Recursive Method 
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)

a = [1, 2, 3, 4, 5]
reverseList(a, 0, 4)
print(a)