import numpy as np
from tabulate import tabulate
import pandas as pd

#  dynamic programming implementation of the chart

npos_left = list(range(6))
margin = list(range(-23,23))
td_score = 0.19
fg_score = 0.13
pt2_score = 0.5
kick_score = 0.94

gd = np.zeros((len(margin),len(npos_left)))
G = np.zeros((len(margin),len(npos_left)))
fd = np.zeros((len(margin),len(npos_left)))
F = np.zeros((len(margin),len(npos_left)))

for i, m in enumerate(margin):
    if m > 0:
        G[margin.index(m),0] = 1
        F[margin.index(m),0] = 1
    if m == 0:
        G[margin.index(m),0] = 0.5
        F[margin.index(m),0] = 0.5
    if m < 0:
        G[margin.index(m),0] = 0
        F[margin.index(m),0] = 0
        
for j, p in enumerate(npos_left):
    if p == 0:
        continue
    for i,m in enumerate(margin):
        g1 = (fg_score*F[margin.index(max(m-3,min(margin))),j-1])+(td_score*kick_score*F[margin.index(max(m-7,min(margin))),j-1])+(td_score*(1-kick_score)*F[margin.index(max(m-6,min(margin))),j-1])+((1-fg_score-td_score)*F[margin.index(m),j-1])
        g2 = (fg_score*F[margin.index(max(m-3,min(margin))),j-1])+(td_score*pt2_score*F[margin.index(max(m-8,min(margin))),j-1])+(td_score*(1-pt2_score)*F[margin.index(max(m-6,min(margin))),j-1])+((1-fg_score-td_score)*F[margin.index(m),j-1])
        f1 = (fg_score*G[margin.index(min(m+3,max(margin))),j-1])+(td_score*kick_score*G[margin.index(min(m+7,max(margin))),j-1])+(td_score*(1-kick_score)*G[margin.index(min(m+6,max(margin))),j-1])+((1-fg_score-td_score)*G[margin.index(m),j-1])
        f2 = (fg_score*G[margin.index(min(m+3,max(margin))),j-1])+(td_score*pt2_score*G[margin.index(min(m+8,max(margin))),j-1])+(td_score*(1-pt2_score)*G[margin.index(min(m+6,max(margin))),j-1])+((1-fg_score-td_score)*G[margin.index(m),j-1])
        if g1 <= g2:
            gd[margin.index(m),j] = 1
        else:
            gd[margin.index(m),j] = 2
        if f1 >= f2:
            fd[margin.index(m),j] = 1
        else:
            fd[margin.index(m),j] = 2
        G[margin.index(m),j] = min(g1,g2)
        F[margin.index(m),j] = max(f1,f2)


row_names = margin
col_names = npos_left

F_df = pd.DataFrame(data=F, index=row_names, columns=col_names)
print(tabulate(F_df, headers='keys', tablefmt='psql'))

fd_df = pd.DataFrame(data=fd, index=row_names, columns=col_names)
print(tabulate(fd_df, headers='keys', tablefmt='psql'))
