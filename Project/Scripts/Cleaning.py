import os
import csv
import pandas as pd 
import numpy as np

# This function recives a file name like "DD_MM_YYYY.csv"
# Return the datetime DD/MM/YYYY
def getDateFromFileName(file_name):
    date_file = pd.to_datetime(file_name.split('.')[0].replace('_','/'))
    return date_file

# Main function
def main():
    path = './../DataSet/AirBnB/'
    dataframes = []


    for directory in os.listdir(path):
        for name_file in os.listdir(path + '/' + directory):
            date_file = getDateFromFileName(name_file)

            # Getting original data of ---
            datos = pd.read_csv(path + '/' + directory + '/' + name_file, header=0)
            df = pd.DataFrame(datos)

            # Completing empty values --- comodin 01012000
            df['reviews_per_month'] = df['reviews_per_month'].fillna(value=0)
            day_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2000')).dt.day
            month_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2000')).dt.month
            year_last_review = pd.to_datetime(df['last_review']).fillna(value=pd.to_datetime('01/01/2000')).dt.year

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

            # Adding dataframe to dataframes list
            dataframes.append(df)

            
    # Joining all the dataframes
    join = pd.concat(dataframes)

    # saving the new csv file
    join.to_csv(path + "airbnb.csv", index=False)


if __name__ == "__main__":
    main()