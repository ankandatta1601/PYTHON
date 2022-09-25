import logging as ln
import os

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
arr = [[1,2,3],
        [4,5,6],
        [7,8,9]]

arr2 = [[1,2,3,8],
        [4,5,6,9],
        [7,8,9,10],
        [10,11,12,16]]


ln.basicConfig(filename='diagonal.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def diagonaldiff(arr):
    try:
        d1 = 0
        d2 = 0
        diff = 0
        for i in range(len(arr)):
            d1+= arr[i][i]
            ln.info('d1 --> Primary diagonal of the array: {}'.format(d1))
            d2+= arr[i][len(arr)-i-1]
            ln.info('d2 --> Secondary diagonal of the array: {}'.format(d2))
            diff = abs(d1-d2)
            ln.info('func: {} - {} = {}'.format(d1, d2, diff))
    except Exception as e:
        print(e)
        ln.info('error: {}'.format(e))
    return diff

diagonaldiff(arr)
diagonaldiff(arr2)




