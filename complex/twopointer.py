import logging as ln

ln.basicConfig(filename='TwoPointer.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

arr = [1,2,3,4,4,5]

target = 6

def TwoPointer(arr, target):
    try:
        ln.info('Array is ,: {}'.format(arr))
        ln.info('Target is ,: {}'.format(target))
        arr.sort()
        l = 0
        r = len(arr)-1
        count = 0
        try:
            while l<r:
                if arr[l]+ arr[r]==target:
                    print(arr[l], arr[r])
                    ln.info('First, second elements with target are : {}, {}, {}'.format(arr[l], arr[r], target))
                    count+=1
                    l+=1
                    r-=1
                elif arr[l]+arr[r]<target:
                    ln.info('When target is Greater First, second elements with target are : {}, {}, {}'.format(arr[l], arr[r], target))
                    l+=1
                else:
                    ln.info('When target is Lesser First, second elements with target are : {}, {}, {}'.format(arr[l], arr[r], target))
                    r-=1
        except Exception as e:
            ln.error('error occured,: {}'.format(e))
    except Exception as e:
        ln.error('error occured,: {}'.format(e))


print(TwoPointer(arr,target))