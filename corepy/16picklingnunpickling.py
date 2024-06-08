##Pickle and UnPickle
## Pickle in Python is primarily used in searalizing and desearializing a Python object structure.
# In other words, it's the process of coverting a Python object into a byte stream to store it in a file/database,
# maintain program state across sessions, or transport data over the network

import seaborn as sns 

df = sns.load_dataset('tips')  # load tips dataset
print(df.head())

import pickle 

filename='file.pkl'

#Searalize process
pickle.dump(df,open(filename,'wb'))  #dump(object,open file in wb mode)
# here pikle.dump() will dump whole df object in file.pkl by searlizing object

#Unsearlize
df1=pickle.load(open(filename,'rb'))
print(type(df1))
print(df1.head())

# Another example
dic_example = {'first_name':'Riddhi','last_name':'Shrestha'}
pickle.dump(dic_example,open('test.pkl','wb'))

print(pickle.load(open('test.pkl','rb')))