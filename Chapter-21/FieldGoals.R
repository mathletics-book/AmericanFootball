###########################################################################
### Chapter 21 - Football Decision Making 101                           ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

library(readr)
library(stats)
library(ggplot2)

dataset <- read_csv("fieldgoals.csv")

## run the logistic regression model
f <- as.formula("Good ~ Distance")
logitfit <- glm(f, data = dataset, family = binomial())

print(summary(logitfit))

## visualize the results
ggplot(dataset, aes(x = Distance, y = Good)) +
  geom_point() +
  geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
  ylab("Success Probability")
ggsave("FG.png")

