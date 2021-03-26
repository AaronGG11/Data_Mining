import os
import csv
import pandas as pd 
import numpy as np

def main():
    path = './../DataSet/AirBnB/2021/23_02_2021.csv'

    datos = pd.read_csv(path, header=0)
    print(datos.info())

if __name__ == "__main__":
    main()