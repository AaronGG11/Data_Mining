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


def main():
    dimenciones = ["espacio", "tiempo", "tipo", "dias_minimos"]

    #imprime_ordenado(combinaciones(dimenciones, 3))
    #print(numero_combinaciones(4,2))
    #print_array(combinaciones_intermedias(dimenciones))

    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port
    server = 'localhost' 
    database = 'airbnb' 
    username = 'Garcia' 
    password = '123456' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    #Sample select query
    cursor.execute("SELECT * from alcaldias") 


    for row in cursor:
        print(row)
    
    



if __name__ == "__main__":
    main()

