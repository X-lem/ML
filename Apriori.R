# Apriori

# install.packages('arules')
library(arules)

# Importing the dataset as a sparse matrix
# ds = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
ds = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
summary(ds)
itemFrequencyPlot(ds, topN = 50)

# Training Apriori on the dataset
rules = apriori(data = ds, parameter = list(support = 0.004, confidence = 0.2))

# Visualizing the results
inspect(sort(rules, by = 'lift')[1:20])