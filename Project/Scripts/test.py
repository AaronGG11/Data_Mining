import os
import csv
import pandas as pd 
import numpy as np

def main():
    path = './../DataSet/TARGET/'
    file = 'metrobus.csv'

    datos = pd.read_csv(path + file, header=0)
    print(datos.info())
    #print(datos.columns.values)

if __name__ == "__main__":
    main()