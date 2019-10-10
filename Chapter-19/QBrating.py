###########################################################################
### Chapter 19 - Who’s better: Brady or Rodgers?                        ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
from tabulate import tabulate

QBdata = pd.read_csv("QBdata.csv")

## calculate the TRUOPASS and the OINTRATE

QBdata['TRUOPASS'] = (QBdata['Yds']-QBdata['SackYards'])/QBdata['Att']
QBdata['OINTRATE'] = QBdata['Int']/QBdata['Att']

## calculate the QB rating based on Brian Burke's regression
QBdata['OurRating'] = (1.543*QBdata['TRUOPASS']) - (50.0957*QBdata['OINTRATE'])

print(tabulate(QBdata[['Player','OldQBR','TOTALQBR','OurRating']], headers='keys', tablefmt='psql'))

# correlation matrix
print("++++++++++++++++++++++ Correlation Matrix ++++++++++++++++++++++")
corr = QBdata[['OldQBR','TOTALQBR','OurRating']].corr()

print(corr)
