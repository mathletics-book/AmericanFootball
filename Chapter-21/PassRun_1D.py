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

print("Pass-Run Ration on 1st and 10 at our own 25")
print(dataset["play_type"].value_counts())


pass_epa = dataset[dataset.play_type == "pass"]["epa"]
run_epa = dataset[dataset.play_type == "run"]["epa"]

matplotlib.rcParams.update({'font.size': 15})


fig = plt.figure()
ax1 = fig.add_axes(ylim=(-8,8))
ax2 = fig.add_axes(ylim=(-8,8))
sns.distplot(pass_epa,ax = ax1,label="Pass")
sns.distplot(run_epa,ax = ax2,label="Run")
plt.xlabel("Expected Points Added")
plt.ylabel("Probability Density")
plt.legend()
plt.savefig("Pass-Run-EPA.png")

