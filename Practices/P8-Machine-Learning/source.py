import os
import csv
import datetime
import pandas as pd 
import numpy as np
from tabulate import tabulate

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score,accuracy_score
from sklearn.preprocessing import StandardScaler

def removeOutliers(data, value, low_percentil, high_percentil):
    min_thresold = data[value].quantile(low_percentil)
    max_thresold = data[value].quantile(high_percentil)
    
    return data[(data[value] >= min_thresold) & (data[value] <= max_thresold)]
    

def main():    
    path = "../../DataSet/project/TARGET/"
    main_file = "airbnb.csv"
    
    # Obtener datos de fuente original
    data_x = ["neighbourhood", "room_type", "minimum_nights", "calculated_host_listings_count"]
    data_y = "price"
    data = data_x + [data_y]
    
    main_df = pd.read_csv(path + main_file, usecols=data)
    main_df = main_df.sample(frac = 1)
    main_df = main_df.head(-1)
    
    
    # Eliminar valores atipicos de algunas columnas 
    data_to_put_off_outliers = ['price','calculated_host_listings_count', 'minimum_nights']
    
    for value in data_to_put_off_outliers:
        main_df = removeOutliers(main_df,value, 0.05, 0.95)
    
    
    # Separar datos en conjunto de entrenamiento y pruebas
    df_x = main_df[data_x]
    df_y = main_df[data_y]
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2)
    
    
    # Aplicar modelo de aprendizaje de maquina
    clf = SVR(C=1.0, epsilon=0.2)
    parametersSVM = {"C":  [1,10,100, 1000, 10000,100000],
              "gamma": [0.1,0.01,0.001,0.0001,1,10,100]}

    gs_clf = GridSearchCV(clf, parametersSVM, n_jobs=-1)
    gs_clf = gs_clf.fit(x_train,y_train)
    gs_clf.best_score_ 
    rbf_svc_tunning = gs_clf.best_estimator_

    y_svm2 = rbf_svc_tunning.fit(x_train, y_train)
    score2=rbf_svc_tunning.score(x_train, y_train)
    crossvalue = cross_val_score(rbf_svc_tunning, x_train, y_train, cv = 10)
    res2=rbf_svc_tunning.predict(x_test)
    
    # Presentacion de resultados
    table = []
    
    for index, item in enumerate(res2):
        #aux = []
        error = (abs(y_test.iloc[index] - item) / y_test.iloc[index]) * 100
        
        #aux.append(y_test.iloc[index], item, error)
        table.append([y_test.iloc[index], item, str(error) + " %"])
        
    print(tabulate(table, headers=['Real','Prediccion', 'Error' ],tablefmt="grid", numalign="center"))
    
    print("-------------------------------------------------")
    print(rbf_svc_tunning.score(x_test, y_test))
    print("-------------------------------------------------")
    

if __name__ == "__main__":
    main()