###########################################################################
### Chapter 25 - NFL Overtime   ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

data <- read.csv("NFL-OT.csv")

# We use only games that ended up with a winner
ind <- data$homescore != data$awayscore
ind20122017 <- data$season >= 2012

datasetfinal <- data[ind & ind20122017, ]

# Every game gives one datapoint and essentially we model the probability that the team that receives the kickoff at OT wins the game.
# The intercept of this model will essentially capture any impact of having the ball first.
# winCoin will be 1 if the team that received the kickoff won
# spreadCoin will be the point spread from the perspective of the team receiving the kickoff (positive: receiving team is the pregame favorite)

winCoin <- ifelse(datasetfinal$homescore > datasetfinal$awayscore, 1, 0)
spreadCoin <- ifelse(datasetfinal$coin == datasetfinal$home, datasetfinal$spread, -datasetfinal$spread)

datasetfinal$winCoin <- winCoin
datasetfinal$spreadCoin <- spreadCoin

# Model 1: 2012-2017
f1 <- winCoin ~ 1
logitfit1 <- glm(formula = f1, data = datasetfinal, family = binomial())

cat("########################################## Model 1: 2012-2017 ##########################################\n")
summary(logitfit1)


# Model 2: 2012-2017
f2 <- winCoin ~ spreadCoin
logitfit2 <- glm(formula = f2, data = datasetfinal, family = binomial())

cat("########################################## Model 2: 2012-2017 ##########################################\n")
summary(logitfit2)

