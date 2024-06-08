# Seaborn
## Distribution plots
# distplot
# joinplot
# pairplot

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')
print(df.head())

# Correlation with heatmap
## A correlation heatmap uses colored cells, typically in monochromatic scale, 
# to show a 2D correlation matrix (table) between two discrete dimensions or event types.
# It is very important in Feature selection

# Compute the correlation matrix, excluding non-numeric columns
cor = df.select_dtypes(include='number').corr()

# Print the correlation matrix
print(cor)

plt.figure(figsize=(10,8))
sns.heatmap(cor,annot=True,linewidth=0.5,fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# JointPlot
#-> A joint plot allows to study the relationship between 2 numeric variables. The central chart
# display their corrlation. It is usually a scatterplot, a hexbin plot, a 2 D histogram
# or a 2D density plot

# Univariate Analysis

sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')
plt.title('Univariate Analysis using Joint Plot')
plt.show()


sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')
plt.title('Univariate Analysis using Joint Plot')
plt.show()

# Pair plot
#-> A "pairs plot" is also known as a scatterplot, in which one variable
# in the same data row is matched with another variable's value, like this:
# Pairs plots are just elaborations on this, showing all variables paired with all 
# the other variables
sns.pairplot(df)
plt.title("Pair plot")
plt.show()


sns.pairplot(df, hue='sex')
plt.title("Pair plot")
plt.show()

# Dist plot
#-> Dist plot helps us to check the distribution of the columns feature.
sns.distplot(df['tip'])
plt.title("Dist plot")
plt.show()

sns.distplot(df['tip'],kde=False,bins=10)
plt.title("Dist plot --")
plt.show()

# Categorical Plots
#-> Seaborn also helps us in doing the analysis on Categorical Data points.
# In this section we discuss about: boxplot,violinplot,countplot,bar plot

# Count plot
sns.countplot(data=df,x="sex")
plt.title("Count plot")
plt.show()

sns.countplot(data=df,y="sex")
plt.title("Count plot")
plt.show()

# Bar plot
sns.barplot(data=df,x='total_bill',y='sex')
plt.title("Bar plot")
plt.show()

sns.barplot(data=df,x='sex',y='total_bill')
plt.title("Bar plot--")
plt.show()

# Box plot: A box and whisker plot (sometimes called a boxplot) is a graph that
# represents informaton from a five-number summary
sns.boxplot(data=df,x='smoker',y='total_bill')
plt.title("Box plot")
plt.show()

sns.boxplot(data=df,x='day',y='total_bill',palette='rainbow')
plt.title("Box plot**")
plt.show()

sns.boxplot(data=df,orient='v')
plt.title("**--Box plot--**")
plt.show()
#categorize data based on some other category
sns.boxplot(data=df,x='total_bill',y='day',hue='smoker')
plt.title("box plot with some other category")
plt.show()

# Violin plot
#-> Violin plot helps us to see both the distribution of data in terms of kernal density
# estimation and the box plot.
sns.violinplot(data=df,x='total_bill',y='day',palette='rainbow')
plt.title("Violin plot")
plt.show()