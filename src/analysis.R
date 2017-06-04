library(dplyr)
library(ggplot2)

res = read.csv('results.csv')
colnames(res) = c('game_id', 'winner', 'player0_mean', 'player1_mean', 'num_turns')

res %>% ggplot(aes(x =factor(winner), y=player0_mean)) + geom_boxplot()
res %>% ggplot(aes(x =factor(winner), y=player0_mean)) + geom_violin()
res %>% ggplot(aes( x=player0_mean)) + geom_histogram()
