# Get the highest of the 1st array
def myfunc(arr1, arr2):
    a1_max = max(arr1)
    a2_min = min(arr2)
    
    start = a1_max
    end = a2_min
    flag = 1
    count = 0
    
    for num in range(start,end+1):
        
        for each in arr1:
            if num % each != 0:
                flag = 1
                break
            else:
                flag = 0
        
        if flag == 1:
            continue
        
        for each in arr2:
            if (each % num != 0 and flag == 1):
                flag = 1
                break
            else:
                flag = 0
                
        if flag == 0:
            count += 1
            flag = 1
            
        print("number:",num, " count:",count)
        
    print("tot_count:",count)  
    
#example
myfunc([3,4], [24,48])
            
    
    
    
    
