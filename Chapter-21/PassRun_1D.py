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

## data obtained from nflscrapR - Yurko, Ventura, Horowitz (2019)
dataset = pd.read_csv("pbp_1618.csv")

print("Pass-Run Ration on 1st and 10 at our own 25")
print(dataset["play_type"].value_counts())

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
