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


arr2 = [8,9,6,8,52,8,55,74,89,98,54,21,5,8,56,2,1,2,14,14,58,98,65,20,0,200,54,15,48,59,98,36,12,15,54,54,88,54,21,87,7]

print(leader_element(arr2))