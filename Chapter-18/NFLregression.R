###########################################################################
### Chapter 18 - What Makes NFL Teams Win?                              ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

library(readr)
library(dplyr)
library(stats)
library(lmtest)

nfldata <- read_csv("NFLdata.csv") %>%
  rename(RET_TD = `RET TD`) %>%
  rename(PY_A = `PY/A`) %>%
  rename(DPY_A = `DPY/A`) %>%
  rename(RY_A = `RY/A`) %>%
  rename(DRY_A = `DRY/A`)

# full regression model
nflmodel <- lm(Margin ~ RET_TD + PENDIF + PY_A + DPY_A + RY_A + DRY_A + TO + DTO - 1, data = nfldata)
print(summary(nflmodel))

# passing-only regression
nflmodelpassing <- lm(Margin ~ PY_A + DPY_A, data = nfldata)
print(summary(nflmodelpassing))

# rushing-only regression
nflmodelrushing <- lm(Margin ~ RY_A + DRY_A, data = nfldata)
print(summary(nflmodelrushing))

# correlation matrix
cat("++++++++++++++++++++++ Correlation Matrix ++++++++++++++++++++++\n")
corr_cols <- nfldata %>% select(-Year, -Margin) %>% select_if(is.numeric)
corr <- cor(corr_cols)
print(corr)

