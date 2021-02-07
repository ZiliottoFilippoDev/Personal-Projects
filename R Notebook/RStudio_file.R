#import data
library(datasets)

#see data
head(iris)
summary(iris)

#plot data
plot(iris)

#clear plots
dev.off()

#to download packages cran.r-project.org
#packges-task view

#load package manager
install.packages('pacman')
require(pacman)
library(pacman)

pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis, httr,
               lubridate, plotly, rio, rmarkdown, shiny,
               stringr, tidyr)

p_load(psych)
library(plotly)
p_load(plotly, ggplot2)

fig <- plot_ly(
  x = c("giraffes", "orangutans", "monkeys"),
  y = c(20, 14, 23),
  name = "SF Zoo",
  type = "bar"
)

fig