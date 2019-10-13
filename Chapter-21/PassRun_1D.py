###########################################################################
### Chapter 21 - Football Decision Making 101                           ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("pbp_1618.csv")
#epv = pd.read_csv("CWS.csv")

print("Pass-Run Ration on 1st and 10 at our own 25")
print(dataset["play_type"].value_counts())


#epa = [(epv[(epv.Down == 2) & (epv.Ydstogo == 10-dataset['yards_gained'].iloc[i])& (epv.Line == 25+dataset['yards_gained'].iloc[i])]["Value"].reset_index()['Value'][0]-epv[(epv.Down == 1) & (epv.Ydstogo == 10) & (epv.Line == 25)]["Value"].reset_index()['Value'][0]) if dataset['yards_gained'].iloc[i] < 10 else (epv[(epv.Down == 1) & (epv.Ydstogo == min(10,100-(25 + dataset['yards_gained'].iloc[i]))) & (epv.Line == 25 + dataset['yards_gained'].iloc[i])]["Value"].reset_index()['Value'][0]-epv[(epv.Down == 1) & (epv.Ydstogo == 10) & (epv.Line == 25)]["Value"].reset_index()['Value'][0]) for i in range(len(dataset))]


pass_epa = dataset[dataset.play_type == "pass"]["epa"]
run_epa = dataset[dataset.play_type == "run"]["epa"]

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("The average EPA for a pass play is: ", np.mean(pass_epa), " with a success rate of: ", len([x for x in pass_epa if x>0])/len(pass_epa))
print("The average EPA for a run play is: ", np.mean(run_epa), " with a success rate of: ", len([x for x in run_epa if x>0])/len(run_epa))

matplotlib.rcParams.update({'font.size': 15})

plt.figure()
plt.subplot(211)
sns.distplot(pass_epa,label="Pass")
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.xlabel("Expected Points Added")
plt.ylabel("Density")
plt.legend()

plt.subplot(212)
sns.distplot(run_epa,label="Run")
plt.yticks([0,0.2,0.4,0.6,0.8])
plt.xlabel("Expected Points Added")
plt.ylabel("Density")
plt.legend()

plt.savefig("Pass-Run-EPA.png")
