install.packages("tidyverse")
install.packages("ggplot2")
library(ggplot2)
privacy.data <- read.csv(file="sentiment.csv")

## Country
### Bar Chart to visualize the sentiment of state-based legislation by country
country_sentiment <- ggplot(aes(x=country, y=score, color=score, fill=country), data = privacy.data) + 
  geom_bar(stat = "identity")
country_sentiment+ labs(title = "Privacy Legislation Sentiment by Country", x = "Country", y = "Sentiment Score")
plot(country_sentiment)

## Region
### Bar Chart to visualize the sentiment of state-based legislation by region
region_sentiment <- ggplot(aes(x=region, y=score, color=region, fill=region), data = privacy.data) + 
  geom_bar(stat = "identity")
region_sentiment+ labs(title = "Privacy Legislation Sentiment by Region", x = "Region", y = "Sentiment Score")
plot(region_sentiment)

## Assessment Type
### Bar Chart to visualize the sentiment of state-based legislation by assessment type
type_sentiment <- ggplot(aes(x=type, y=score, color=type, fill=type), data = privacy.data) + 
  geom_bar(stat = "identity")
type_sentiment+ labs(title = "Privacy Legislation Sentiment by Type of Assessment", x = "Assessment Type", y = "Sentiment Score")
plot(type_sentiment)

## Sector
### Bar Chart to visualize the sentiment of state-based legislation by sector
sector_sentiment <- ggplot(aes(x=sector, y=score, color=sector, fill=sector), data = privacy.data) + 
  geom_bar(stat = "identity")
sector_sentiment+ labs(title = "Privacy Legislation Sentiment by Sector", x = "Sector", y = "Sentiment Score")
plot(sector_sentiment)
