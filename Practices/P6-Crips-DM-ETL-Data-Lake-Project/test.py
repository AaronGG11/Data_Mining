import os
import csv
import datetime
import pandas as pd 
import numpy as np

def generateCatalogueRoomType():
    path = "./DataSet/project/TARGET/"
    file_1 = "airbnb.csv"
    target_file = "room_type_catalogue.csv"

    data_df = pd.read_csv(path + file_1)
    dict_room_type = dict((j,i) for i,j in enumerate(set(data_df["room_type"].tolist())))
    dict_rt = enumerate(set(data_df["room_type"].tolist()))
    df = pd.DataFrame(dict_rt, columns = ['id', 'room_type'])

    df.to_csv(path + target_file, index=False)


def exchangeRoomTypeById(dictionary, value):
    return dictionary[value]


def getFinalAirBnB():
    path = "./DataSet/project/TARGET/"
    main_file = "airbnb.csv"
    catalogue_file = "room_type_catalogue.csv"
    target_file = "airbnb_final.csv"

    main_df = pd.read_csv(path + main_file)
    catalogue_df = pd.read_csv(path + catalogue_file)

    dictionary = dict(zip(catalogue_df["room_type"].to_list(), catalogue_df["id"].to_list()))

    # Exchange delegacion by delegacion id
    main_df["room_type"] = main_df["room_type"].apply((lambda x: exchangeRoomTypeById(dictionary, x)))

    main_df.to_csv(path + target_file, index=False)


def main():
    path = "./DataSet/project/TARGET/"
    main_file = "airbnb.csv"

    main_df = pd.read_csv(path + main_file)

    print(main_df.info())


if __name__ == "__main__":
    main()

