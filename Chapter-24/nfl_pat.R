###########################################################################
### Chapter 24 - Should We Go for One-Point or Two-Point Conversion?    ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

library(tidyverse)

f_reg <- file("pat.csv", "w")
writeLines("Team;Year;Attemp2pt;Success2pt;Attemptkick;Successkick", con = f_reg)

# Simulating data for demonstration
for (yy in 2009:2018) {
  for (w in 1:17) {
    # Simulating game scores
    if (runif(1) < 0.5) {
      s <- "Team A 7 - Team B 0 (kick is good)"
      cat(paste0(sub("\\s.*", "", s), ";", yy, ";0;0;1;1\n"), file = f_reg, sep = "")
    } else {
      s <- "Team A 7 - Team B 0 (kick is missed)"
      cat(paste0(sub("\\s.*", "", s), ";", yy, ";0;0;1;0\n"), file = f_reg, sep = "")
    }
    if (runif(1) < 0.5) {
      s <- "Team A 6 - Team B 0 (fail)"
      cat(paste0(sub("\\s.*", "", s), ";", yy, ";1;0;0;0\n"), file = f_reg, sep = "")
    } else {
      s <- "Team A 6 - Team B 0"
      cat(paste0(sub("\\s.*", "", s), ";", yy, ";1;1;0;0\n"), file = f_reg, sep = "")
    }
  }
}

close(f_reg)

dataset <- read.csv("pat.csv", sep = ";", stringsAsFactors = FALSE)

conversion_rates <- dataset %>%
  group_by(Year) %>%
  summarise(`2pt` = sum(Success2pt) / sum(Attemp2pt),
            Kick = sum(Successkick) / sum(Attemptkick)) %>%
  pivot_longer(-Year, names_to = "Type", values_to = "ConversionRate") %>%
  pivot_wider(names_from = "Type", values_from = "ConversionRate") %>%
  column_to_rownames("Year")

conversion_rates

