import os
import csv
import datetime
import pandas as pd 
import numpy as np
import itertools




# Main function
def algo(valor):
    x = 1 + valor

    return x


def main():
    path = './../DataSet/CDMX/'
    target_file = "delegaciones.csv"

    datos = pd.read_csv(path + target_file, header=0)
    df = pd.DataFrame(datos)
    df = df.dropna()

    dictionary = dict(zip(df["Alcaldía"].to_list(), df["id"].to_list()))


    print(df["Alcaldía"].apply((lambda x: algo(1))))



if __name__ == "__main__":
    main()