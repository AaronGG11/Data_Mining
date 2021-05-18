# Script for AirBnB data cleaning

import os
import csv
import datetime
import pandas as pd 
import numpy as np

# This function recives a file name like "DD_MM_YYYY.csv"
# Return the datetime DD/MM/YYYY
def getDateFromFileName(file_name):
    date_file = pd.to_datetime(file_name.split('.')[0].replace('_','/'))
    return date_file

def exchangeNeigbourhoodByIdNeigbourhood(dictionary, value):
    return dictionary[value]

# Main function
def main():
    start_time = datetime.datetime.now()

    path = './../DataSet/AIRBNB/'
    target_file = "airbnb.csv"
    delegaciones_file = './../DataSet/CDMX/delegaciones.csv'
    dataframes = []

    # Detelete target file if this exists
    if os.path.exists(path + target_file):
        os.remove(path+target_file)

    # Read delegaciones directory
    data = pd.read_csv(delegaciones_file, header=0)
    d_f = pd.DataFrame(data)
    d_f = d_f.dropna()

    dictionary = dict(zip(d_f["Alcaldía"].to_list(), d_f["id"].to_list()))


    for directory in os.listdir(path):
        print("\nDirectorio " + directory + " :")

        for name_file in os.listdir(path + '/' + directory):
            print("\tProcesando " + name_file + " ...")

            date_file = getDateFromFileName(name_file)

            # Getting original data of ---
            datos = pd.read_csv(path + '/' + directory + '/' + name_file, header=0)
            df = pd.DataFrame(datos)

            # Completing empty values --- comodin 01012000
            df['reviews_per_month'] = df['reviews_per_month'].fillna(value=0)

            df['last_review'] = df['last_review'].fillna(value=pd.to_datetime('01/01/2000'))
            day_last_review = pd.to_datetime(df['last_review']).dt.day
            month_last_review = pd.to_datetime(df['last_review']).dt.month
            year_last_review = pd.to_datetime(df['last_review']).dt.year

            # Pulling away last review date in day, month and year ---
            # df = df.assign(day_last_review=day_last_review)
            df = df.assign(month_last_review=month_last_review)
            df = df.assign(year_last_review=year_last_review)

            # Adding month and year of data file ---
            # df = df.assign(date_data=date_file)
            df = df.assign(month_data=date_file.month)
            df = df.assign(year_data=date_file.year)

            # Removing last_review, host_name and neighbourhood_group columns
            df = df.drop(['last_review'], axis=1)
            df = df.drop(['host_name'], axis=1)
            df = df.drop(['neighbourhood_group'], axis=1)

            # Exchange delegacion by delegacion id
            df["neighbourhood"] = df["neighbourhood"].apply((lambda x: exchangeNeigbourhoodByIdNeigbourhood(dictionary, x)))

            # Adding dataframe to dataframes list
            dataframes.append(df)

            
    # Joining all the dataframes
    join = pd.concat(dataframes)

    # Removing nan rows
    join.dropna(how="all", inplace=True)

    # saving the new csv file
    join.to_csv(path + target_file, index=False)

    # Swowing data info
    print("\nResumen de archivo objetivo")
    print(join.info())

    end_time = datetime.datetime.now()
    diference = end_time - start_time 
    print("\nTiempo de procesamiento: " + str(diference.seconds) + " segundos")


if __name__ == "__main__":
    main()