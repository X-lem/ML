# Random Selection

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
ds = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Random Selection
import random
N = 10000
d = 10
adSelected = []
totalReward = 0
for n in range(0, N):
    ad = random.randrange(d)
    adSelected.append(ad)
    reward = ds.values[n, ad]
    totalReward = totalReward + reward

# Visualising the results
plt.hist(adSelected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()