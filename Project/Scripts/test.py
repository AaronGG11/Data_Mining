import os
import csv
import pandas as pd 
import numpy as np

def main():
    path = './../Tests/airbnb.csv'

    datos = pd.read_csv(path, header=0)
    print(datos)
    #print(datos.info())
    #print(datos.columns.values)

if __name__ == "__main__":
    main()