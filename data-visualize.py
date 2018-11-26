import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("data/house-regression/train.csv")
print(train.SaleType)

plt.figure(1)
sns.pointplot(x=train.SaleType, y=train.SalePrice)


plt.figure(2)
g = sns.pointplot(x=train.Neighborhood, y=train.SalePrice)
g.set_xticklabels(train.Neighborhood, rotation=45)

plt.figure(3)
g = sns.FacetGrid(train, col="SaleType")
g = g.map(plt.hist, "SalePrice")

plt.show()


