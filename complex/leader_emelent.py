import logging as ln

ln.basicConfig(filename='leader_element.log', level=ln.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

arr = [16,17,4,3,5,2]
# print(len(arr)-1, len(arr), sep = '\t')
def leader_element(arr):
    try:
        ln.info('Array is : {}'.format(arr))
        maximum = arr[len(arr)-1]
        print(maximum)
        ln.info('Maximum Value(default) is,: {}'.format(maximum))
        for i in range(len(arr)-2, 0, -1):
            #print(i,arr[i], sep = '\t')
            if arr[i]>maximum:
                maximum = arr[i]
                ln.info('Updated maximum is,: {}'.format(maximum))
                print(maximum)
    except Exception as e:
        ln.error('error occured,: {}'.format(e))
        
print(leader_element(arr))
print(leader_element([12,15,3,2,6,25,8,9]))