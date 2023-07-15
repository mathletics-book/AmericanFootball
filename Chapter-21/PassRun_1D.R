###########################################################################
### Chapter 21 - Football Decision Making 101                           ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

library(readr)
library(ggplot2)
library(scales)

dataset <- read_csv("pbp_1618.csv")

cat("Pass-Run Ratio on 1st and 10 at our own 25:\n")
cat(table(dataset$play_type), "\n")

pass_epa <- dataset$epa[dataset$play_type == "pass"]
run_epa <- dataset$epa[dataset$play_type == "run"]

cat("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
cat("The average EPA for a pass play is:", mean(pass_epa), "with a success rate of:", sum(pass_epa > 0) / length(pass_epa), "\n")
cat("The average EPA for a run play is:", mean(run_epa), "with a success rate of:", sum(run_epa > 0) / length(run_epa), "\n")

# Plotting the distributions
ggplot(dataset, aes(x = epa, fill = play_type)) +
  geom_density(alpha = 0.5) +
  ylab("Density") +
  xlab("Expected Points Added") +
  scale_y_continuous(labels = percent) +
  facet_wrap(~ play_type, nrow = 2, scales = "free") +
  theme_minimal() +
  theme(legend.position = "none")

ggsave("Pass-Run-EPA.png", width = 8, height = 10, units = "in")

