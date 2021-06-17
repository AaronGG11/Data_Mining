import os
import csv
import datetime
import pandas as pd 
import numpy as np

def main():
    path = "../../DataSet/project/TARGET/"
    main_file = "airbnb.csv"

    main_file = pd.read_csv(path + main_file)
    print(main_file.info())




if __name__ == "__main__":
    main()