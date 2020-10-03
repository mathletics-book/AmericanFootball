import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf



data = pd.read_csv("NFL-OT.csv")

## We use only games that ended up with a winner
ind = data["homescore"] != data["awayscore"]
ind20122017 = data["season"] >= 2012

datasetfinal = data[ind & ind20122017]



### Every game gives one datapoint and essentially we model the probability that the team that receives the kickoff at OT wins the game. The intercept of this model will essentially capture any impact of having the ball first
#winCoin will be 1 if the team that received the kickoff won
#spreadCoin will be the point spread from the perspective of the team receiving the kickoff (positive: receiving team is the pregame favorite)

winCoin = []
spreadCoin = []


for i in datasetfinal.index.tolist():
    if datasetfinal["homescore"][i] > datasetfinal["awayscore"][i]:
        winteam = datasetfinal["home"][i]
    else:
        winteam = datasetfinal["away"][i]
    if datasetfinal["coin"][i] == winteam:
        winCoin.append(1)
    else:
        winCoin.append(0)
    if datasetfinal["coin"][i] == datasetfinal["home"][i]:
       spreadCoin.append(datasetfinal["spread"][i])
    else:
       spreadCoin.append(-datasetfinal["spread"][i])

datasetfinal["winCoin"] = winCoin
datasetfinal["spreadCoin"] = spreadCoin

f1 = "winCoin~1"

logitfit1 = smf.glm(formula = str(f1), data = datasetfinal,family=sm.families.Binomial()).fit()
print("########################################## Model 1: 2012-2017 ##########################################")
print(logitfit1.summary())

f2 = "winCoin~spreadCoin"

logitfit2 = smf.glm(formula = str(f2), data = datasetfinal,family=sm.families.Binomial()).fit()
print("########################################## Model 2: 2012-2017 ##########################################")
print(logitfit2.summary())

