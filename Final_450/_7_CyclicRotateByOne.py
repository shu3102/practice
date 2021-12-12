#User function Template for python3

def rotate( arr, n):
    t = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = t
    return arr

#Time Complexity: O(n) As we need to iterate through all the elements 
#Auxiliary Space: O(1)




def rotate2( arr, n):
    return arr.insert(0, arr.pop())
     

# Method 2
# two pointer swap
def rotate3(arr, n):
    i = 0
    j = n-1
    while(i != j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr



#  Driver Code Starts
#Initial Template for Python 3
def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)
        T -= 1

if __name__ == "__main__":
    main()
