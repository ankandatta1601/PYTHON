import logging as ln

ln.basicConfig(filename='Prefixsum.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def PrefixSum(arr):
    ln.info('Array is ,: {}'.format(arr))
    try:
        for i in range(1,len(arr)):
            arr[i] = arr[i-1]+arr[i]
            ln.info('Elemental componnents are : {}'.format(arr[i]))
            ln.info('Updated Array is  : {}'.format(arr))
    except Exception as e:
        ln.error('error occured,: {}'.format(e))
    ln.info('Final Array is ,: {}'.format(arr))
    return arr

arr = [10,20,10,5,15]
print(PrefixSum(arr))
print(PrefixSum([3,1,2,10,1]))
print(PrefixSum([1,2,3,4]))
print(PrefixSum([1,1,1,1,1]))