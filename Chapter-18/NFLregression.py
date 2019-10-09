###########################################################################
### Chapter 18 - What Makes NFL Teams Win?                              ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

nfldata = pd.read_csv("NFLdata.csv")

nflmodel = ols('Margin~RETTD+PENDIF+PY_A+DPY_A+RY_A+DRY_A+TO+DTO-1',data = nfldata).fit()

nflmodel.summary()
