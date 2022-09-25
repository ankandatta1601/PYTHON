import logging as ln

ln.basicConfig(filename='binary_search.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
arr = [1,2,3,4,5,5]
key1 = 1
key2 = 20
key3 = 5
def binary_search(arr,target):

    ''' 
        BINARY SEARCH ALGORITHM : 
        While going from L-->R values are increasing
        arr : Array
        key : Value to be searched
        While moving to the right, ignore the left part and vice versa knowing that L<R
        We will not be travelling the complete Array thus TC will not be greater than O(N)
        
    '''
    try:
        ln.info('Array is ,: {}'.format(arr))
        ln.info('Target is ,: {}'.format(target))
        low = 0
        ln.info('Initial low Value is,: {}'.format(low))
        high = len(arr) - 1
        ln.info('Initial high Value is,: {}'.format(high))
        middle = 0
    
        while low <= high:  
            middle = (high + low) // 2
            ln.info('Updated Middle Value is,: {}'.format(middle))
            
            # target equals arr[middle], return middle (index of target)
            if target == arr[middle]: 
                ln.info('Updation for Middle Value is,: {}'.format(middle))
                return middle
            # Take the upper half 
            elif target > arr[middle]: 
                low = middle + 1
                ln.info('Updated Low Value is,: {}'.format(low))
    
            # Take the lower half
            else: 
                high = middle - 1
                ln.info('Updated high Value is,: {}'.format(high))
    
        # If we reach this line, target is not present in arr
        ln.info('Value not found thus returning,: {}'.format(-1))
        return -1
    except Exception as e:
        ln.error('error occured,: {}'.format(e))


print(binary_search(arr, 3))
print(binary_search(arr, key1))
print(binary_search(arr, key2))
print(binary_search(arr, key3))