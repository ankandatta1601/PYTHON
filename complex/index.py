import logging as ln
ln.basicConfig(filename='index.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s:%(Matrix must be a square matrix)s')

arr = [5,2,1,3,4,-6,-2]
key = -2
def index(arr, key):
    try:
        ans = -1
        ln.info('Array is --> : {}'.format(arr))
        ln.info('Value to be searched is --> : {}'.format(key))
        for i in range(len(arr)):
            ln.info('Index,Value,Key: {},{}, {}'.format(i, arr[i],key))
            if arr[i] == key:
                ln.info('When MAtches --> Index,Value,Key: {},{}, {}'.format(i, arr[i],key))
                ans =  i
                ln.info('Index for the value is --> : {}'.format(ans))
                return ans
   
        ln.info('Index for the value is when absent is --> : {}'.format(ans))
        return ans
    except Exception as e:
        ln.info('error  --> : {}'.format(e))
index(arr,key)