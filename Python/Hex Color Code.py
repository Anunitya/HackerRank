import re
N = int(input())

for _ in range(N) : 
    text = input().strip()
    codes = [j for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})',text,re.IGNORECASE)]
    for code in codes :
        print(code)
        
        
        
    '''
    It's a regex: [\s:] will match either a space of a colon. That way it filters out the ones right at the beginning of the line
    [a-f0-9]{6} will match hexes that start with hashtag followed by six hex digis (0-9a-f)
    [a-f0-9]{3} Same as above with 3
    re.I is to ignore the case
    '''
    
