
def find(arr,n,x):
    # code here
    first = -1
    last = -1
    
    for i in range(n):
        if(arr[i] != x):
            continue
        if(first == -1):
            first = i
        last = i
            
    return first, last

def find1(arr,n,x):
    # code here
    mn = mx = -1
    for i in range(n):
        if(arr[i] == x):
            mn = i
            break
    for i in range(n-1, -1, -1):
        if(arr[i] == x):
            mx = i
            break
    return mn, mx

# Another approach using binary search 
#iterate loop two times first for first element and next loop for last element 


        
