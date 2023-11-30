def breakingRecords(scores):
    maxscore = minscore = scores[0]
    max_break = min_break = 0
    flag = 0
    
    for each in scores:
        if each > maxscore:
            maxscore = each
            max_break += 1
            flag = 1
        
        if each < minscore and flag == 0:
            minscore = each
            min_break += 1
            flag = 0
            
        flag = 0
            
    return [max_break, min_break]
