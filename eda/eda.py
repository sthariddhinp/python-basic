# EDA: Exploratory Data Analysis (EDA)

# import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data
train = pd.read_csv('titanic_train.csv')
print(train.head())

# Exploratory Data Analysis
## Missing Data
#-> we can use seaborn to create a simple heatmap to see where we are missing data.
print(train.isnull())   # True means it has NaN value in the column

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train)
plt.show()

# survived rate based on gender
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,hue='Sex',palette='RdBu_r')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,hue='Pclass',palette='rainbow')
plt.show()