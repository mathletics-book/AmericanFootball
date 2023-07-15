###########################################################################
### Chapter 19 - Who’s better: Brady or Rodgers?                        ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

library(readr)
library(dplyr)
library(tidyr)

QBdata <- read_csv("QBdata.csv")

## calculate the TRUOPASS and the OINTRATE
QBdata <- QBdata %>%
  mutate(TRUOPASS = (Yds - SackYards) / Att,
         OINTRATE = Int / Att)

## calculate the QB rating based on Brian Burke's regression
QBdata <- QBdata %>%
  mutate(OurRating = (1.543 * TRUOPASS) - (50.0957 * OINTRATE))

cat("++++++++++++++++++++++ Player Ratings ++++++++++++++++++++++\n")
QBdata_ratings <- QBdata %>%
  select(Player, OldQBR, TOTALQBR, OurRating) %>%
  rename("Old QBR" = OldQBR, "TOTAL QBR" = TOTALQBR)
print(as.data.frame(QBdata_ratings))

# correlation matrix
cat("++++++++++++++++++++++ Correlation Matrix ++++++++++++++++++++++\n")
corr <- QBdata %>%
  select(OldQBR, TOTALQBR, OurRating) %>%
  cor()
print(corr)

