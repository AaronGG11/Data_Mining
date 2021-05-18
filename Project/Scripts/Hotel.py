import os
import csv
import datetime
import pandas as pd 
import numpy as np
import itertools


def exchangeNeigbourhoodByIdNeigbourhood(dictionary, value):
    return dictionary[value]

def getCategoryOk(category):
    aux = category.split()

    if(category == 'Sin Clasificar'):
        return 0
    else:
        return aux[0]


def main():
    start_time = datetime.datetime.now()

    path = './../DataSet/CDMX/'
    target_directory = './../DataSet/TARGET/'
    hotels = 'hoteles.csv'
    delegaciones = "delegaciones.csv"
    target_file = "hotels.csv"

    # Detelete target file if this exists
    if os.path.exists(target_directory + target_file):
        os.remove(target_directory + target_file)

    datos_1 = pd.read_csv(path + delegaciones, header=0)
    df_1 = pd.DataFrame(datos_1)
    df_1 = df_1.dropna()

    dictionary = dict(zip(df_1["Alcaldía"].to_list(), df_1["id"].to_list()))

    datos_2 = pd.read_csv(path + hotels, header=0)
    df_2 = pd.DataFrame(datos_2)
    df_2 = df_2.dropna()

    # Exhanging deleghacion by delegacion id
    print("Sustituyendo nombre de delegacion por id de delegacion ...")
    df_2['alcaldia']= df_2['alcaldia'].apply((lambda x: exchangeNeigbourhoodByIdNeigbourhood(dictionary, x)))


    # Removing last_review, host_name and neighbourhood_group columns
    print("Eliminando dimensiones: calle_y_numero, cp, colonia ...")
    df_2 = df_2.drop(['calle_y_numero'], axis=1)
    df_2 = df_2.drop(['colonia'], axis=1)
    df_2 = df_2.drop(['cp'], axis=1)

    # Setting caterory format
    # Exchange delegacion by delegacion id
    df_2["categoria"] = df_2["categoria"].apply((lambda x: getCategoryOk(x)))

    # saving the new csv file
    print("Obteniendo formato de categoria correcto por estrellas ...")
    df_2.to_csv(target_directory + target_file, index=False)

    # Swowing data info
    print("\nResumen de archivo objetivo")
    print(df_2.info())

    end_time = datetime.datetime.now()
    diference = end_time - start_time 
    print("\nTiempo de procesamiento: " + str(diference.seconds) + " segundos")



if __name__ == "__main__":
    main()