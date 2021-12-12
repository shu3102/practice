# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 3
# rotate array by shifting the elements
def RotateByShift(arr, n, d):
    part1 = arr[:d]
    for i in range(n - d):
        arr[i] = arr[i + d]
    for i in range(n - d, n):
        arr[i] = part1[i - n + d]
    #print(arr)
    return arr 

# Method 2
# two pointer swap
 
