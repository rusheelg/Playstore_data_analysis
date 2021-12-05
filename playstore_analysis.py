

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

g_url = "https://raw.githubusercontent.com/rusheelg/Playstore_ratings_analysis/main/playstore_data.csv"
gdata = pd.read_csv(g_url)

gdata.head(5)

#cleaning
gdata.isnull().sum()

#Ratings more than 5 - an outlier
gdata[gdata.Rating > 5]

#dropping it since it isn't a True Value
gdata.drop([10472], inplace=True)

#confirming that the index value has been dropped
gdata.loc[10470:10475]

#checking for outlier values thorough a histogram/boxplot 
gdata.hist()

#removing columns that are 90% empty
treshold = len(gdata) * 0.1
treshold

gdata.dropna(thresh=treshold, axis=1,inplace=True)
gdata.isnull().sum()

#Data manipulation - fill missing rows with mean, median or mode
def impute_median(x):
  return x.fillna(x.median())

gdata.Rating = gdata['Rating'].transform(impute_median)

#recheck for null values
gdata.isnull().sum()

#finding out mode values for data
print(gdata.Type.mode())
print(gdata['Current Ver'].mode())
print(gdata['Android Ver'].mode())

#filling in the mode values for the missing str data
gdata['Type'].fillna(str(gdata['Type'].mode().values[0]), inplace=True)
gdata['Current Ver'].fillna(str(gdata['Current Ver'].mode().values[0]), inplace=True)
gdata['Android Ver'].fillna(str(gdata['Android Ver'].mode().values[0]), inplace=True)

#count the missing values to confirm the above
gdata.isnull().sum()

gdata.head(2)

# convert price, reviews and ratings into numerical data
gdata['Price'] = gdata['Price'].apply(lambda x:str(x).replace('$','') if '$' in str(x) else str(x))
gdata['Price'] = gdata['Price'].apply(lambda x: float(x))
gdata['Reviews'] = pd.to_numeric(gdata['Reviews'], errors='coerce')

gdata['Installs']
gdata['Installs'] = gdata['Installs'].apply(lambda x:str(x).replace(',','') if ',' in str(x) else str(x))
gdata['Installs'] = gdata['Installs'].apply(lambda x:str(x).replace('+','') if '+' in str(x) else str(x))
gdata['Installs'] = gdata['Installs'].apply(lambda x: float(x))

gdata.head()

gdata.describe()

grp = gdata.groupby('Category')
x = grp['Rating'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Reviews'].agg(np.mean)
print(x)
print(y)
print(z)

# Data Visualization for Ratings
plt.figure(figsize=(12,6))
plt.plot(x, 'ro', color='blue')
plt.xticks(rotation=90)
plt.title("Category wise Rating")
plt.xlabel('Categories -->')
plt.ylabel('Ratings-->')
plt.show()

# Data Visualization for Prices
plt.figure(figsize=(12,6))
plt.plot(y, 'r--', color='red')
plt.xticks(rotation=90)
plt.title("Category wise Pricing")
plt.xlabel('Categories -->')
plt.ylabel('Pricing-->')
plt.show()

# Data Visualization for Reviews
plt.figure(figsize=(12,6))
plt.plot(z, 'g^', color='green')
plt.xticks(rotation=90)
plt.title("Category wise Reviews")
plt.xlabel('Categories -->')
plt.ylabel('Reviews-->')
plt.show()