###########################################################################
### Chapter 24 - Should We Go for One-Point or Two-Point Conversion?    ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import nflgame
import numpy as np
import pandas as pd
from tabulate import tabulate

f_reg = open("pat.csv","w")

print("Team;Year;Attemp2pt;Success2pt;Attemptkick;Successkick",file=f_reg)

for yy in [2009,2010,2011,2012,2013,2014,2015,2016]:
	for w in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
		games = nflgame.games(yy,week=w,kind="REG") 
		for i in range(len(games)):
			for k in range(len(games[i].scores)):
				s = games[i].scores[k]
				if "TD" in s:
					x = s[s.find("(")+1:s.find(")")]
					if "kick" in x:
						if "kick is good" in x:
							print(s.split("-")[0].rstrip(),";",yy,";",0,";",0,";",1,";",1,file=f_reg)
						else:
							print(s.split("-")[0].rstrip(),";",yy,";",0,";",0,";",1,";",0,file=f_reg)
					else:
						if "fail" in x:
							print(s.split("-")[0].rstrip(),";",yy,";",1,";",0,";",0,";",0,file=f_reg)
						else:
							print(s.split("-")[0].rstrip(),";",yy,";",1,";",1,";",0,";",0,file=f_reg)

f_reg.close()
conversion_rates = dict()

dataset = pd.read_csv("pat.csv",delimiter=";")

for year, dataset_season in dataset.groupby('Year'):
	conversion_rates[year] = {'2pt': np.sum(dataset_season['Success2pt'])/np.sum(dataset_season['Attemp2pt']), 'Kick': np.sum(dataset_season['Successkick'])/np.sum(dataset_season['Attemptkick'])}

print(tabulate(pd.DataFrame.from_dict(conversion_rates), headers='keys', tablefmt='psql'))
	
