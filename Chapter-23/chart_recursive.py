import numpy as np

## This implementation will work well for few possessions left (e.g., up to 5) but will be extremely slow for more possessions left

def G_function(npos_left, margin, fg_score, td_score, pt2_score, kick_score):
    if npos_left == 0:
        if margin > 0:
            return 1, 1, 0, 0
        if margin == 0: 
            return 0.5, 0.5, 0, 0
        if margin < 0:
            return 0, 0, 0, 0
    else:
        f1 = fg_score*G_function(npos_left-1, margin+3, fg_score, td_score, pt2_score, kick_score)[0]+td_score*kick_score*G_function(npos_left-1, margin+7, fg_score, td_score, pt2_score, kick_score)[0]+td_score*(1-kick_score)*G_function(npos_left-1, margin+6, fg_score, td_score, pt2_score, kick_score)[0]+(1-fg_score-td_score)*G_function(npos_left-1,margin, fg_score, td_score, pt2_score, kick_score)[0]
        f2 = fg_score*G_function(npos_left-1, margin+3, fg_score, td_score, pt2_score, kick_score)[0]+td_score*pt2_score*G_function(npos_left-1, margin+8, fg_score, td_score, pt2_score, kick_score)[0]+td_score*(1-pt2_score)*G_function(npos_left-1, margin+6, fg_score, td_score, pt2_score, kick_score)[0]+(1-fg_score-td_score)*G_function(npos_left-1,margin, fg_score, td_score, pt2_score, kick_score)[0]
        g1 = fg_score*G_function(npos_left-1, margin-3, fg_score, td_score, pt2_score, kick_score)[1]+td_score*kick_score*G_function(npos_left-1, margin-7, fg_score, td_score, pt2_score, kick_score)[1]+td_score*(1-kick_score)*G_function(npos_left-1, margin-6, fg_score, td_score, pt2_score, kick_score)[1]+(1-fg_score-td_score)*G_function(npos_left-1,margin, fg_score, td_score, pt2_score, kick_score)[1]
        g2 = fg_score*G_function(npos_left-1, margin-3, fg_score, td_score, pt2_score, kick_score)[1]+td_score*pt2_score*G_function(npos_left-1, margin-8, fg_score, td_score, pt2_score, kick_score)[1]+td_score*(1-pt2_score)*G_function(npos_left-1, margin-6, fg_score, td_score, pt2_score, kick_score)[1]+(1-fg_score-td_score)*G_function(npos_left-1,margin, fg_score, td_score, pt2_score, kick_score)[1]
        if f1 >= f2:
            r3 = 1
        else:
            r3 = 2
        if g1 >= g2:
            r4 = 1
        else:
            r4 = 2
        return min(g1,g2), max(f1,f2), r3, r4
        
        
#example
print(1,0,0.13,0.19,0.45,0.94)
