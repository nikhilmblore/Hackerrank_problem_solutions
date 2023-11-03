def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app_count = orange_count = 0
    
    for each in apples:
        each = each+a
        if(each >= s and each <= t):
            app_count +=1
            
    for each in oranges:
        each = each+b
        if(each >= s and each <= t):
            orange_count +=1    
            
    print(app_count)
    print(orange_count)
