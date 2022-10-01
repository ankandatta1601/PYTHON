
def find_dups():

    #inp =input('enter string : ')
    inp = 'google.com'

    inp = inp.replace('.', '')
    l = []

    for i in inp:
        l.append(i)


    d = {}
    l2 = []
    
    for i in range(len(l)): 
        for j in range(i+1, len(l)):
            if l[i]==l[j]:
                l2.append(l[i])

        print('l2 ', l2, sep = '\t)
        for m in range(len(l2)):
     
            if ord(l[i]) == ord(l2[m]):
                counter=0
                print('l[i] ', l[i],'l2[m]', l2[m], 'counter ', counter, sep = '\t')
                for keys, values in d:
                    d[keys] = l[i]
                    d[values] = counter
                    counter+=1
                #d.update({l[i]:counter})
            else:
                counter = 1
          
        # if l[i] in l2:
        #     print(l[i], counter, sep = '\t')
        #     d.update({l[i]:counter})
        #     counter+=1
        # else:
        #     d.update({l[i]:1})

    
    return d




find_dups()