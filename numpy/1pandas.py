## Pandas
#-> Pandas is an open source, BSD-licensed library providing high-performance,easy-to-use data structures and data analysis tools for the Python programming language.

#1. What is Data Frames?
#2. What is Data Series?
#3. Different operation in Pandas




import pandas as pd 
import numpy as np

# Dataframe: It is a combination of both columns and rows and it will basically shows you representaion format how it looks like in excelsheet data.
## DataFrame contains data,index's name and column's name
## DataFrame is a combination of many many columsn and rows.(altest greater than 1 rows and 1 columns)
df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['Column1','Column2','Column3','Column4'])   # index is no of rows i.e. 5 , and column is no of columns i.e.4
print(df.head())
df.to_csv('Test1.csv')

## Accessing the elements:
# There are two ways to access elements from your Dataframe
#1) .loc(focus on row index)  2) .iloc (index location:focus on both row & column indexes)
print(df.loc['Row1'])
# See what is it's type i.e. type(df.loc['Row1'])
print(type(df.loc['Row1']))
# we can see it is pandas.core.series.Series i.e. It is a Series type.

# Series: Series can be either 1 row or 1 column.

print(df.iloc[:,:])     #.iloc[row_index,column_index]
print(df.iloc[0:2,0:2])
print(type(df.iloc[0:2,0:2]))
print(type(df.iloc[0:2,0:1]))
print(type(df.iloc[0:2,0]))
# If we have atleast more than one columen then it is Dataframe.

# Dataframe can also be converted into Array
# i.e. It is going to skip column index and row index from dataframe.
print(type(df.iloc[:,1:].values))   # this .value will converting your dataframe into array
print(df.iloc[:,1:].values.shape)

# EDA
# Check if any Null value in your Dataframe?
print(df.isnull().sum())
# How to check uniue categorical value in my specific column?
print(df['Column1'].value_counts())
print(df['Column1'].unique())

# You can directly access your dataframe value directly by calling Column'name directly too
print(df['Column4'])  # access one column
print(type(df['Column4']))
print(df[['Column4','Column2']])  # access two or multiple columns

## Pandas Read ###
df = pd.read_csv("mercedesbenz.csv")
print(df.head())

print(df.info())          # information about DataFrame
print(df.describe())      # provide stastical description about dataset and it will only consider your numerical/integer/float column.

print(df['X0'].value_counts())   # Get the unique category counts

print(df[df['y']>100])

## CSV
from io import StringIO, BytesIO

data = ('col1,col2,col3\n'
            'x,y,1\n'
            'a,b,2\n'
             'c,d,3')

print(type(data))

print(pd.read_csv(StringIO(data)))
## Read from specific columns
df = pd.read_csv(StringIO(data),usecols=['col1','col2'])
print(df.head())

df.to_csv('Test.csv')  # save data into csv
# Specifying columns data types
data = ('a,b,c,d\n'
            '1,2,3,4\n'
            '5,6,7,8\n'
             '9,10,11,12')

print(data)
df = pd.read_csv(StringIO(data),dtype=object)  #dtype=int,float,object
print(df.head())

print(df['a'])
# Specify different dtype for different column
df = pd.read_csv(StringIO(data),dtype={'b':int,'c':float,'a':'Int64'})
print(df['c'])
# Check dtypes of all columns of df
print(df.dtypes)

# define index column
data = ('index,a,b,c\n'
        '4,apple,bat,4,7\n'
        '8,oragne,cow,10')
df = pd.read_csv(StringIO(data),index_col=0)  # index 0 will be row index here
print(df)

data = ('a,b,c\n'
        '4,apple,bat,4,\n'
        '8,oragne,cow,')
df = pd.read_csv(StringIO(data))
print(df.head())

df = pd.read_csv(StringIO(data),index_col=False)
print(df.head())

## combining usecols and index_col
df = pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False)
print(df.head())

## Quoting and Escape Characters. Very useful in NLP
data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'
df = pd.read_csv(StringIO(data),escapechar='\\')
print(df.head())

# URL to CSV
# df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',sep='\t')
# print(df.head())

## Read JSON to CSV
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
df = pd.read_json(Data)
print(df.head())

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
print(df.head())

# convert json to csv
df.to_csv('wine.csv')
#convert json to different format
print(df.to_json(orient="index"))
print(df.to_json(orient="records"))

## Reading HTML content
# url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
# dfs = pd.read_html(url)
# print(dfs[0])

# url_mcc = 'https://en.wikipedia.org/wiki/Mobile_country_code'
# dfs = pd.read_html(url_mcc, match='Country', header=0)
# print(dfs[0])

# Reading Excel Files
df_excel = pd.read_excel('SampleExcel.xlsx')
print(df_excel.head())

# Pickling
# All pandas objects are equipped with to_pickle methods which use Python’s cPickle module to save data structures to disk using the pickle format.
df_excel.to_pickle('df_excel')
df=pd.read_pickle('df_excel')
print("Data from pickle file.")
print(df.head())