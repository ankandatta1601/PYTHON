#Question 1:  Given an array of N integers. Your task is to print the sum of all of the integers.

def sum_of_elements_in_a_list(l):

    print('+'*50)
    print('QUESTION 1 :')
    print('+'*50, '\n\n')
    ''' L will be a list of numbers '''
    
    counter = 0
    print('List is :', l, '\n')
    for i in range(0,len(l)):
        counter = counter + l[i]
        print('Index', i, 'Element ', l[i], 'SUM ',counter)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')

    print('ANSWER NO 1 IS',counter, '\n\n')
sum_of_elements_in_a_list([1,2,3,4])
sum_of_elements_in_a_list([5, 8, 3, 10, 22 ,45])

#Question2 : Given an array A[] of N integers and an index Key. Your task is to print the element present at index key in the array

def integers_and_index(index, array): 
    print('+'*50)
    print('QUESTION 2 :')
    print('+'*50, '\n\n')
    ''' index = Index array,
        array = array'''
    print('INDEX ARRAY : ', index)
    print('--------------------------------------')
    print('ARRAY : ', array)
    print('----------------------------------------')
    idx = 0
    for i in range(0,len(index)):
        idx = index[i]
        


    print('ANSWER 2 IS :', array[idx], '\n\n')

integers_and_index([5, 2], [10, 20, 30, 40, 50])
integers_and_index([7, 4], [10, 20, 30, 40, 50, 70])

#Question 3 : Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

def less_than_or_equal(a,x):
    print('+'*50)
    print('QUESTION 3 :')
    print('+'*50, '\n\n')
    ''' a = array;
        x = value;
        n = length of a '''

    print('ORIGINAL LIST :', a)
    print('+'*50)
    a.sort()
    print('SORTED LIST :', a)
    print('+'*50)
    n = len(a)
    
    print('N : ', n)
    print('X : ', x)

    l =[]

    unique_list = []

    for i in range(0, len(a)):
        if x >= a[i]:
            l.append(a[i])
    print('Appended list is :', l, '\n')
    print('++++++++++++++++++++++++++')
    print('ANSWER 3 IS :', len(l), '\n\n')

less_than_or_equal([1, 2, 4, 5, 8, 10], 9)
less_than_or_equal([1, 2, 2, 2, 5, 7, 9], 2)

#Question 4 : You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).


def alternate(a):

    print('+'*50)
    print('QUESTION 4 :')
    print('+'*50, '\n\n')
    '''a = array'''
    l = []
    for i in range (0, len(a),2):
        l.append(a[i])
    print('ANSWER 4 :', l, '\n\n')

alternate([1, 2, 3, 4])
alternate([1, 2, 3, 4, 5])

#Question 5 : Given an array Arr of N positive integers. Your task is to find the elements whose value is equalto that of its index value ( Consider 1-based indexing ).

def same_as_index(arr):

    print('QUESTION 5 :')
    print('+'*50, '\n\n')
    ''' Arr = ARRAY'''
    N = len(arr)
    print('N : ', N, '\n\n')
    l = []
    for i in range(0, len(arr)):
        z = i+1
        print('INDEX IS : ', z, '->'*10, 'THE ITEM CORRESPONDING TO THE INDEX IS : ', arr[i], '\n\n')
        if z == arr[i]:
            x = arr[i]
            l.append(x)
    print('THE ANSWER TO QUESTION 5 IS',l, '\n\n', '+++'*10)

same_as_index([15, 2, 45, 12, 7])
same_as_index([1])

#Question 6 : Given an array of size N and you have to tell whether the array is perfect or not. An array is said to be perfect if it's reverse array matches the original array. If the array is perfect then print "PERFECT" else print "NOT PERFECT". 

def perfect_check(arr):
    
    print('QUESTION 6 :')
    print('+'*50, '\n\n')
    arr2 = arr[::-1]
    if arr == arr2:
        print('ANSWER 6 : PERFECT')
    else :
        print('ANSWER 6 : NOT PERFECT')

perfect_check([1, 2, 3, 2, 1])
perfect_check([1, 2, 3, 4, 5])

#Question 7 : Given an array of length N, at each step it is reduced by 1 element. In the first step the maximumelement would be removed, while in the second step minimum element of the remaining array would be removed, in the third step again the maximum and so on. Continue this till the array contains only 1 element. And find the final element remaining in the array.


def step_array(arr):
  
    ''' arr : array '''

    print('QUESTION 7 :')
    print('+'*50, '\n\n')
    length = len(arr)
    print('ARRAY INPUT : ', arr, '\n', 'LENGTH : ', length)
    for i in range(0,len(arr)): 

      if len(arr)>2:
        print('Step No : ', i, '\n <<<<<<<<<<<<<<<<->>>>>>>>>>>>>>>>>>>>>>>>>>>')
        arr.remove(max(arr))
        arr.remove(min(arr))
        print('max : ', max(arr), '\n min : ', min(arr))
        print('ARRAY : ', arr)
        print('UPDATED ARRAY : ', arr)

        if len(arr)==2:
          arr.remove(max(arr))
          print('UPDATED ARRAY HERE THE LENGHTH OF THE ARRAY == 2: ', arr)

    print('ANSWER 7 : ', arr)

step_array([7, 8, 3, 4, 2, 9, 5])
step_array([8, 1, 2, 9, 4, 3, 7, 5])

#Question 8 : Given an array of N distinct elements, the task is to find all elements in array except two greatest elements in sorted order.

def findElements(arr):
    ''' arr : array '''

    print('QUESTION 8 :')
    print('+'*50, '\n\n')
    length = len(arr)
    print('ARRAY INPUT : ', arr, '\n', 'LENGTH : ', length)
    arr.sort()
    l = []
    for i in range(0, len(arr)-2):
        l.append(arr[i])
    print('ANSWER 8 : ',l, '\n')
 

findElements([2, 8, 7, 1, 5])
findElements([7, -2, 3, 4, 9, -1])

#Question 9 : Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)

def sum_of_n(n):

  ''' n : range '''

  print('\n QUESTION 9 : \n')
  print('+'*50, '\n\n')
  print('YOUR RANGE IS : ', n)
  count = 0
  arr = []
  for i in range(0, n+1):
    arr.append(i)
    print('STEP : ', i, '--------------------------->', arr)
    count+= arr[i]
    print('SUM : ',count)
  print("ANSWER 9 IS : ", count)

sum_of_n(1)
sum_of_n(5)





