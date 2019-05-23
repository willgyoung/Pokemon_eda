# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:06:59 2019

@author: William
"""

import pandas as pd

#Changes how wide the text display is
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 320)

df = pd.read_csv("pokemon_data.csv")

print(df.head(5))

print(df.columns)

print(df['Name'])

fireType = df.loc[df["Type 1"] == "Fire"]

fireType.head()

df.describe()

df.sort_values('Name', ascending = False)
df.sort_values('Attack', ascending = False)


df.head()

col_list = list(df)
col_list.remove('#')
col_list.remove('Generation')

#Sums along the horizontal axis (0 sums vertically)
df['Total'] = df[col_list].sum(axis=1)
df.head()

cols = list(df.columns)

#Changes the order of the columns
dfNew = df[cols[0:10] + [cols[-1]] + cols[10:12]]
dfNew.head()

fireType.describe()

import re


#looks for names that start with M and ignores case sensitivity
dfNew.loc[df['Name'].str.contains('^m[a-z]*', flags=re.I, regex=True)].sort_values('#')




dfNew.groupby('Type 1').mean().sort_values('Total', ascending = False)

df.groupby('Type 1').count()['#'].sort_values(ascending = False)

df.sort_values('Total', ascending = False)

#Creates a top 5 dataframe
top5 = df.sort_values(['Type 1', 'Total'], ascending = [1,0]).groupby('Type 1').head(5)

#Does the same thing but uses apply function 
df.groupby('Type 1').apply(lambda df: df.nlargest(5, 'Total'))


import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x='Type 1', y = 'Total', data = df)
sns.barplot(x='Type 1', y = 'Total', data = df)

plt.scatter(x = 'Type 1', y = 'Total', data = df)


#%% Changes the size parameters of the displayed figures
fig_size = plt.rcParams["figure.figsize"]
print ("Current size:", fig_size)

fig_size[0] = 14
fig_size[1] = 8

plt.rcParams["figure.figsize"] = fig_size



#%%
plt.scatter(x = 'Type 1', y = 'Total', data = df)

sns.stripplot(x = 'Type 1', y = 'Total', data = df, jitter = 0.2, size = 7)
plt.title('Power level by type', loc='center')

#Filters out based on a string condition
nonMega = dfNew.loc[~dfNew['Name'].str.contains('Mega')]
nonMega.head()

top5nonMega = nonMega.sort_values(['Type 1','Total'], ascending = [1,0]).groupby('Type 1').head(5)
top5nonMega

sns.stripplot(x = 'Type 1', y = 'Total', data = top5nonMega, jitter = 0.2, size = 7)

Pokemon = list(top5nonMega['Name'])
x_coords = list(top5nonMega['Type 1'])
y_coords = list(top5nonMega['Total'])

#Creates a scatter plot that inputs the names 
for i, name in enumerate(Pokemon):
    x = x_coords[i]
    y = y_coords[i]
    plt.scatter(x, y)
    plt.text(x, y, name)
plt.show()


#Filters out based on string condition and boolean condition
noMegaLegend = dfNew.loc[(~dfNew['Name'].str.contains('Mega')) & (dfNew['Legendary'] != True)]
top5noMegaL = noMegaLegend.sort_values(['Type 1', 'Total'], ascending = [1,0]).groupby('Type 1').head(5)


typeStats = df.groupby('Type 1').describe()

dfNew.head()

dfNew.groupby('Type 1').describe()

#Performs descriptive statistics on chosen columns
typeStats = dfNew.loc[:, 'Type 1':'Total'].groupby('Type 1').describe()

#Flips columns and rows
typeStats = pd.DataFrame.transpose(typeStats)


typeStats.to_csv("TypeStats.csv", index = True)
top5.to_csv("Top5_per_type.csv", index = False)

noMegaLegend.sort_values('Total', ascending = False)

