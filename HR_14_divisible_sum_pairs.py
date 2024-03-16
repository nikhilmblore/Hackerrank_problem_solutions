def divisibleSumPairs(n, k, ar):
    # Write your code here
    
    result = []
    count  = 0
    for i in range(0,n):
        
        for j in range(i+1,n):
            if(ar[i]+ar[j])%k==0:
                
                print(i,j)
                pair = ((i,j),(ar[i], ar[j]))
                result.append(pair)
                count = count + 1
                
    return count
    
