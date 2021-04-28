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
    estaciones_id = {}

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

        # ADDING YEAR NUMBER COLUMN
        year_number = df["FECHA"].dt.year
        df.insert(loc = 1, column = "ANIO", value = year_number, allow_duplicates = False)

        # ADDING MONTH NUMBER COLUMN
        month_number = df["FECHA"].dt.month
        df.insert(loc = 2, column = "MES", value = month_number, allow_duplicates = False)

        # ADDING WEEK NUMBER COLUMN
        week_number = df["FECHA"].dt.week
        df.insert(loc = 3, column = "SEMANA", value = week_number, allow_duplicates = False)

        dataframes.append(df)

    # GETTING STATION ID'S
    estaciones = pd.read_csv(path + "estaciones.csv", index_col=None)
    df_estaciones = pd.DataFrame(estaciones)
    estaciones_id = dict(zip(list(df_estaciones["Clave"]), list(df_estaciones["id"])))


    # DATA FRAME TO FACT TABLE
    joining = pd.concat(dataframes).reset_index(drop=True)

    df_ft = pd.DataFrame(columns=["elemento", "fecha", "anio", "month", "week", "localizacion","medicion"])  
    dict_original_columns = dict(zip(joining.columns.values, range(len(joining.columns.values))))

    contador = 0
    for row_index in range(0, len(joining)):
        for row_pp in joining.columns.values[4:]:
            df_ft.loc[contador] = ["Precipitación pluvial", 
                                joining.iloc[row_index]["FECHA"],
                                joining.iloc[row_index]["ANIO"],
                                joining.iloc[row_index]["MES"],
                                joining.iloc[row_index]["SEMANA"],
                                estaciones_id[row_pp],
                                joining.iloc[row_index][row_pp]
            ]

            contador += 1

    print(contador)

    df_ft.index.name = "id"
    df_ft.to_csv(path + "pph.csv", index=True)



if __name__ == "__main__":
    main()