a = [1,4,4,4,5,3]

def migra(ar):
    arlen = len(ar)
    
    max = ar[0]
    maxcnt = 0
    
    temp = {}
    
    for i in range(0,arlen):
        if ar[i] not in temp:
            temp[ar[i]] = 1
            
        else:
            temp.update({ar[i]:temp[ar[i]]+1})
            
            
    print(temp)
       
    for key in temp:
        print(key, temp[key])
        if temp[key]>maxcnt:
            maxcnt = temp[key]
            max = key
        elif temp[key]==maxcnt and key < max:
            maxcnt = temp[key]
            max = key
            
    print("---",max)
    
migra(a)
        
