import os
import csv
import datetime
import pandas as pd 
'''
    SCRIPT FOR CLEANING, TRANSFORMING AND VALIDATE THE DATA
'''


def main():
    path = './DataSet/'
    dataframes = []

    for name_file in os.listdir(path + "pph"):
        datos = pd.read_excel(path + "pph" + "/" + name_file, index_col=0)
        df = pd.DataFrame(datos)

        

        dataframes.append(df)

    joining = pd.concat(dataframes)
    joining.to_excel(path + "pph.xls", index=True)


if __name__ == "__main__":
    main()