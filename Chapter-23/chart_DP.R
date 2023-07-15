###########################################################################
### Chapter 24 - Should We Go for One-Point or Two-Point Conversion?    ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

npos_left <- 0:5
margin <- -23:22
td_score <- 0.19
fg_score <- 0.13
pt2_score <- 0.5
kick_score <- 0.94

gd <- matrix(0, nrow = length(margin), ncol = length(npos_left))
G <- matrix(0, nrow = length(margin), ncol = length(npos_left))
fd <- matrix(0, nrow = length(margin), ncol = length(npos_left))
F <- matrix(0, nrow = length(margin), ncol = length(npos_left))

for (i in 1:length(margin)) {
  if (margin[i] > 0) {
    G[i, 1] <- 1
    F[i, 1] <- 1
  } else if (margin[i] == 0) {
    G[i, 1] <- 0.5
    F[i, 1] <- 0.5
  } else if (margin[i] < 0) {
    G[i, 1] <- 0
    F[i, 1] <- 0
  }
}

for (j in 2:length(npos_left)) {
  for (i in 1:length(margin)) {
    if (npos_left[j] == 0) {
      next
    }
    
    g1 <- (fg_score * F[which(margin == pmax(margin[i] - 3, min(margin))), j - 1]) +
      (td_score * kick_score * F[which(margin == pmax(margin[i] - 7, min(margin))), j - 1]) +
      (td_score * (1 - kick_score) * F[which(margin == pmax(margin[i] - 6, min(margin))), j - 1]) +
      ((1 - fg_score - td_score) * F[i, j - 1])
    g2 <- (fg_score * F[which(margin == pmax(margin[i] - 3, min(margin))), j - 1]) +
      (td_score * pt2_score * F[which(margin == pmax(margin[i] - 8, min(margin))), j - 1]) +
      (td_score * (1 - pt2_score) * F[which(margin == pmax(margin[i] - 6, min(margin))), j - 1]) +
      ((1 - fg_score - td_score) * F[i, j - 1])
    f1 <- (fg_score * G[which(margin == pmin(margin[i] + 3, max(margin))), j - 1]) +
      (td_score * kick_score * G[which(margin == pmin(margin[i] + 7, max(margin))), j - 1]) +
      (td_score * (1 - kick_score) * G[which(margin == pmin(margin[i] + 6, max(margin))), j - 1]) +
      ((1 - fg_score - td_score) * G[i, j - 1])
    f2 <- (fg_score * G[which(margin == pmin(margin[i] + 3, max(margin))), j - 1]) +
      (td_score * pt2_score * G[which(margin == pmin(margin[i] + 8, max(margin))), j - 1]) +
      (td_score * (1 - pt2_score) * G[which(margin == pmin(margin[i] + 6, max(margin))), j - 1]) +
      ((1 - fg_score - td_score) * G[i, j - 1])
    
    if (g1 <= g2) {
      gd[i, j] <- 1
    } else {
      gd[i, j] <- 2
    }
    
    if (f1 >= f2) {
      fd[i, j] <- 1
    } else {
      fd[i, j] <- 2
    }
    
    G[i, j] <- min(g1, g2)
    F[i, j] <- max(f1, f2)
  }
}

F_df <- data.frame(F)
names(F_df) <- npos_left
rownames(F_df) <- margin
print(F_df, headers = TRUE, format = "psql")

fd_df <- data.frame(fd)
names(fd_df) <- npos_left
rownames(fd_df) <- margin
print(fd_df, headers = TRUE, format = "psql")
