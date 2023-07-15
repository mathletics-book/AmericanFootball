library(grDevices)
library(geometry)

locations <- matrix(c(89.13, 31.65,
                      86.32, 26.70,
                      90.03, 28.61,
                      87.83, 31.59,
                      88.77, 28.45,
                      87.52, 27.26), ncol = 2, byrow = TRUE)

# calculate the convex hull
ol_hull <- chull(locations)

ol_area <- polyarea(locations[ol_hull, 1], locations[ol_hull, 2])

print(paste0("The area of the OL convex hull is: ", ol_area))


# plot the data

plot(locations, xlim = c(80, 100), ylim = c(0, 50), xlab = "", ylab = "", asp = 1)
points(locations, pch = 20)

hull_edges <- rbind(locations[ol_hull, ], locations[ol_hull[1], ])
lines(hull_edges, col = "red", lwd = 2)
points(locations[ol_hull[1], ], pch = 19, col = "red")

