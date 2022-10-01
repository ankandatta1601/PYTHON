arr = [-7,1,5,2,-4,3,0]

left = 0
right = 0
ir = 0
mid = len(arr)//2

for i in range(0, mid):
    left+= arr[i]

for i in range(mid+1,len(arr)):
    right+=arr[i]

    if left == right:
        ir = mid
    else:
        ir = -1

print(left, right, ir, sep = '\t')