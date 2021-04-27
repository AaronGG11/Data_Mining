import os
import csv
import datetime
import pandas as pd 
import numpy as np

from datetime import datetime
'''
    SCRIPT FOR CLEANING, TRANSFORMING AND VALIDATE THE DATA
'''


def main():
    path = './DataSet/'
    dataframes = []

    for name_file in os.listdir(path + "pph"):
        datos = pd.read_excel(path + "pph" + "/" + name_file, index_col=None)
        df = pd.DataFrame(datos)

        # REMOVING EMPTY ROWS
        df.dropna(how="all", inplace=True)

        # ADDING INDEX COLUMN NAME EQUALS TO ID
        df.index.name = "id"

        # UNIFYING DATE DATA TYPES
        if df["FECHA"].dtype != "datetime64[ns]":
            df["FECHA"] = df["FECHA"].astype(str)
            df["FECHA"] = pd.to_datetime(df["FECHA"])

        # ADDING MONTH NUMBER COLUMN
        month_number = df["FECHA"].dt.month
        df.insert(loc = 1, column = "MES", value = month_number, allow_duplicates = False)

        # ADDING WEEK NUMBER COLUMN
        week_number = df["FECHA"].dt.week
        df.insert(loc = 2, column = "SEMANA", value = week_number, allow_duplicates = False)
        dataframes.append(df)
   
    joining = pd.concat(dataframes).reset_index(drop=True)
    joining.index.name = "ID"

    joining.to_excel(path + "pph.xls", index=True)



if __name__ == "__main__":
    main()