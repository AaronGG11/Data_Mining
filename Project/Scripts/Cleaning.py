import csv
import pandas as pd 
import numpy as np


name_file = '29_01_2021.csv'
date_file = pd.to_datetime(name_file.split('.')[0].replace('_','/'))

# Getting original data of ---

datos = pd.read_csv(name_file, header=0)
df = pd.DataFrame(datos)

# Completing empty values --- 
df['reviews_per_month'] = df['reviews_per_month'].fillna(value=0)
day_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2018')).dt.day
month_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2018')).dt.month
year_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2018')).dt.year

# Pulling away last review date in day, month and year ---

df  = df.assign(day_last_review=day_last_review)
df  = df.assign(month_last_review=month_last_review)
df  = df.assign(year_last_review=year_last_review)

# Adding month and year of data file ---

df  = df.assign(month_data=date_file.month)
df  = df.assign(year_data=date_file.year)

# Removing last_review and neighbourhood_group columns

df = df.drop(['last_review'], axis=1)
df = df.drop(['neighbourhood_group'], axis=1)

df.to_csv(name_file)



#datos['last_review'] = pd.to_datetime(datos['last_review']).fillna(value=pd.to_datetime('01/01/2018'))
#print(datos['last_review'].dt.year)
#print(datos.columns.values)

# delete 'neighbourhood_group' column
# add 'day_last_review' column
# add 'month_last_review' column
# add 'year_last_review' column
# delete 'last_review' column
# 

