
'''
# Timeout 
def equalStacks(h1, h2, h3):
    h1 = h1[::-1] #reversing strings
    h2 = h2[::-1]
    h3 = h3[::-1]
    s1,s2,s3 = map(sum,(h1,h2,h3))
    while h1 and h2 and h3 : #while there are elements left in the arrays
        m = min(s1,s2,s3)
        while s1 > m : s1 -= h1.pop() #if the curr_sum is not equal to min_sum then we pop the top element from list and subtract that from sum  
        while s2 > m : s2 -= h2.pop()
        while s3 > m : s3 -= h3.pop()
    if s1 ==s2 == s3 :
        return s3
    else : 
        return 0 
    
    ''''

#Instead of looping over all 3 arrays we set the while loop condition to match our result
def equalStacks(h1, h2, h3):
    sum1,sum2,sum3 = map(sum,(h1,h2,h3))
    i,j,k=0,0,0
    if (sum1 == sum2 and sum2 == sum3):
        print(sum1)
    while not (sum1==sum2 and sum2==sum3):
        if(sum1 > sum2 or sum1 > sum3):
            while(sum1 > sum2 or sum1 > sum3):
                sum1-=h1[i]
                i += 1
        elif (sum2 > sum1 or sum2 > sum3):            
            while(sum2 > sum1 or sum2 > sum3):
                sum2-=h2[j]
                j += 1
        elif (sum3 > sum1 or sum3 > sum2):
            while(sum3 > sum1 or sum3 > sum2):
                sum3-=h3[k]
                k += 1
  
    return (sum1)
        
