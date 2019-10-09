###########################################################################
### Chapter 18 - What Makes NFL Teams Win?                              ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

nfldata = pd.read_csv("NFLdata.csv")

# full regression model
nflmodel = ols('Margin~RETTD+PENDIF+PY_A+DPY_A+RY_A+DRY_A+TO+DTO-1',data = nfldata).fit()
print(nflmodel.summary())

# passing-only regression
nflmodelpassing = ols('Margin~PY_A+DPY_A',data = nfldata).fit()
print(nflmodelpassing.summary())

# rushing-only regression
nflmodelrushing = ols('Margin~RY_A+DRY_A',data=nfldata).fit()
print(nflmodelrushing.summary())

# correlation matrix
print("++++++++++++++++++++++ Correlation Matrix ++++++++++++++++++++++")
corr = nfldata.drop(columns = ['Year','Margin']).corr()

print(corr)
