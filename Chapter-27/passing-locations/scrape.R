# Original Author: Sarah Mallepalle
# Updates: Konstantinos Pelechrinis & Scott Nestler
# 
# Use BeautifulSoup to scrape https://nextgenstats.nfl.com/ for all available extra-large (1200 x 1200)
# pass chart images and corresponding pass chart data from the NFL seasons since 2017, 
# and save the image and its corresponding data to the folder 'Pass_Charts'.
# 
# Folder format: ./Pass_Charts/[team]/[season]/[week]/{[images], [data]}/[last_name]_[first_name]_[positon].{jpeg, txt}
# Example: 
# 	Image path = ./Pass_Charts/philadelphia-eagles/2017/super-bowl/images/Foles_Nick_QB.jpeg
# 	Data path = ./Pass_Charts/philadelphia-eagles/2017/super-bowl/data/Foles_Nick_QB.txt

library(jsonlite)
library(httr)

teams <- c("arizona-cardinals", "atlanta-falcons", "baltimore-ravens", "buffalo-bills", "carolina-panthers", "chicago-bears", "cincinnati-bengals", "cleveland-browns", "dallas-cowboys", "denver-broncos", "detroit-lions", "green-bay-packers", "houston-texans", "indianapolis-colts", "jacksonville-jaguars", "kansas-city-chiefs", "las-vegas-raiders", "los-angeles-chargers", "los-angeles-rams", "miami-dolphins", "minnesota-vikings", "new-england-patriots", "new-orleans-saints", "new-york-giants", "new-york-jets", "philadelphia-eagles", "pittsburgh-steelers", "san-francisco-49ers", "seattle-seahawks", "tampabay-buccaneers", "tennessee-titans", "washington-football-team")

seasons <- c("2020")

weeks <- c("1", "2", "3")

pattern <- "charts"

for (team in teams) {
  for (season in seasons) {
    cat(paste(team, season, "\n"))
    for (week in weeks) {
      URL <- paste("https://nextgenstats.nfl.com/charts/list/pass/", team, "/", season, "/", week, sep = "")
      r <- tryCatch(GET(URL), error = function(e) NULL)
      
      if (is.null(r)) {
        cat("Failed to retrieve data from:", URL, "\n")
        next
      }
      
      soup <- content(r, as = "text")
      
      script <- regmatches(soup, regexec(pattern, soup))
      
      if (length(script) == 0) {
        cat("LENGTH SCRIPT = 0: No pass chart data found for:", URL, "\n")
        next
      }
      
      contains_charts <- tryCatch(fromJSON(substr(script[[1]], 34, nchar(script[[1]]) - 132)), error = function(e) NULL)
      
      if (is.null(contains_charts) || length(contains_charts$charts$charts) == 0) {
        cat("NO CHARTS: No pass chart data found for:", URL, "\n")
        next
      }
      
      for (chart in contains_charts$charts$charts$charts) {
        name <- paste(chart$lastName, chart$firstName, chart$position, sep = "_")
        chart$team <- team
        
        folder <- paste("Pass_Charts", team, season, week, sep = "/")
        img_folder <- paste(folder, "images", sep = "/")
        data_folder <- paste(folder, "data", sep = "/")
        
        dir.create(img_folder, recursive = TRUE, showWarnings = FALSE)
        dir.create(data_folder, recursive = TRUE, showWarnings = FALSE)
        
        img_file <- paste(img_folder, paste0(name, ".jpeg"), sep = "/")
        url <- paste("https:", chart$extraLargeImg, sep = "")
        
        tryCatch(download.file(url, destfile = img_file), error = function(e) {
          cat("Failed to download image:", url, "\n")
        })
        
        data_file <- paste(data_folder, paste0(name, ".txt"), sep = "/")
        write(toJSON(chart), file = data_file)
      }
    }
  }
}

cat("Done.\n")

