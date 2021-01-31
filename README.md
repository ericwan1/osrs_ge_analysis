# osrs_ge_analysis

### Introduction

Runescape is one of the biggest MMORPGs in the world, and it's Grand Exchange (GE) is a central part of the game. Every week, billions of in-game items are traded in this market. Since some comparisons can be made between the GE and real life asset/stock exchanges, there have been plenty of players who try to draw real world technical analysis into the game. 

### The Repo

osrs_price_to_csv.py scrapes the OSRS GE website using Jagex API to grab GE data on various inputted items. The information is then saved into a csv file. The csv file is used to conduct analysis by osrs_analysis.py. Some visualization is done within osrs_analysis.Rmd using ggplot2. The analysis performed is performed with custom moving averages and various percentage changes in price. 

### Future Thoughts

I intend to add more features to the analysis. I also intend to incorporate some more data science/machine learning applications into this project. This may include figuring out ways to identify the most optimal items for trade, for instance. 
