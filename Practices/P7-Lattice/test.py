import os
import csv
import datetime
import pandas as pd 
import numpy as np
from math import factorial
import pyodbc 


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)


def combinaciones(c, n):
    return [s for s in potencia(c) if len(s) == n]


def numero_combinaciones(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))


def combinaciones_intermedias(c):
    result = []
    for i in range(2, len(c)):
        result.extend(combinaciones(c,i))

    return result


def print_array(array):
    for e in array:
        print(e)


def generar_nombre_cubo(dimensiones):
    result = "Cubo_"

    for index, dimension in enumerate(dimensiones):
        if index != len(dimensiones) - 1:
            result += dimension + "_"
        else:
            result += dimension

    return result



def generate_query_1(dimensions):
    result = "SELECT "

    for index, dimension in enumerate(dimensions):
        result += "[airbnb].[dbo].[airbnb].[" + dimension + "], "

    
    result += "AVG([airbnb].[dbo].[airbnb].[price]) AS 'Precio promedio' "
    result += "INTO [airbnb].[dbo].[" + generar_nombre_cubo(dimensions) + "] "
    result += "FROM [airbnb].[dbo].[airbnb] "


    result += "GROUP BY "

    for index, dimension in enumerate(dimensions):
        if index != len(dimensions) -1:
            result += "[airbnb].[dbo].[airbnb].[" + dimension +"], "
        else: 
            result += "[airbnb].[dbo].[airbnb].[" + dimension +"]"
     
    result += ";"


    return result


def print_result_query(result):
    for row in result:
        print(row)


def generar_info_cubo(dimensiones):
    result = ""

    for dimension in dimensiones:
        result += "{" + dimension + "}"

    result += "{AVG(precio)}"

    return result



def main():
    dimenciones = ["neighbourhood", "room_type", "minimum_nights", "year_data", "month_data"]

    server = 'localhost' 
    database = 'airbnb' 
    username = 'Garcia' 
    password = '123456' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()


    for combinacion in combinaciones_intermedias(dimenciones):
        query = generate_query_1(combinacion)
        print("Generando cubo: " + str(generar_info_cubo(combinacion)) + " ...")
        print(query)
        print("")

        cursor.execute(query)
        cnxn.commit()


if __name__ == "__main__":
    main()

