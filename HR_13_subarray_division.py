def birthday(s, d, m):
    # Write your code here
    result = 0
    for i in range(0,len(s)-m+1):
        
        tempsum = 0
        for j in range(i,i+m):
            tempsum = tempsum + s[j]
            if tempsum>d:
                break;
        
        if tempsum == d:
            result += 1
    
    return result
