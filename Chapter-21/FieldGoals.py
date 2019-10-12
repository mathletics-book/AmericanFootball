###########################################################################
### Chapter 21 - Football Decision Making 101                           ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("fieldgoals.csv")

## run the logistic regression model
f = 'Good~Distance'
logitfit = smf.logit(formula = str(f), data = dataset).fit()

print(logitfit.summary2())

## visualize the results 

sns.set_style(style='white') 
ax = plt.subplot(111)
ax = sns.regplot(x="Distance", y="Good", data=dataset, logistic = True)
plt.ylabel("Success Probability")
plt.savefig("FG.png")
