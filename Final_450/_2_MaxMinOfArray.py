# time complexity of reversing an array is O(n)

arr = [1000, 11, 445, 1, 330, 3000]
# Method 1
# iterative method
mi = mx = arr[0]
for i in arr:
    if(i < mi):
        mi = i
    elif(i > mx):
        mx = i
print(mi, mx)



arr = [1000, 11, 445, 1, 330, 3000]
# Method 2
# Sorting
arr.sort()
print(arr[0], arr[-1])



arr = [1000, 11, 445, 1, 330, 3000]
# Method 3
# python inbuild function
print(min(arr), max(arr))




arr = [1000, 11, 445, 1, 330, 3000]
# Method 4
# 