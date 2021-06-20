import os
import csv
import datetime
import pandas as pd 
import numpy as np

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
    
    #return (data[data.between(min_thresold, max_thresold)])
    
    


def main():    
    path = "../../DataSet/project/TARGET/"
    main_file = "airbnb.csv"
    
    # Obtener datos de fuente original
    data_x = ["neighbourhood", "room_type", "minimum_nights", "year_data", "availability_365", "calculated_host_listings_count"]
    data_y = "price"
    data = data_x + [data_y]
    
    main_df = pd.read_csv(path + main_file, usecols=data)
    main_df = main_df.head(2000)
    
    
    # Eliminar valores atipicos de algunas columnas 
    data_to_put_off_outliers = ['price', 'availability_365','calculated_host_listings_count', 'minimum_nights']
    
    for value in data_to_put_off_outliers:
        main_df = removeOutliers(main_df,value, 0.05, 0.95)
    
    
    # Separar datos en conjunto de entrenamiento y pruebas
    df_x = main_df[data_x]
    df_y = main_df[data_y]
    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2)
    
    
    # Aplicar modelo de aprendizaje de maquina
    clf = SVR(C=1.0, epsilon=0.2)
    clf.fit(x_train, y_train) 
    
    SVR(C=1.0, cache_size=200, coef0=0.0,
    degree=3, gamma='auto', kernel='rbf',
    max_iter=-1,  shrinking=True,
    tol=0.001, verbose=False)
    
    scores = cross_val_score(clf, x_train, y_train, cv = 10)
    res1=clf.predict(x_test)
    
    print(clf.score(x_test, y_test))
    
    index=0
    for element in res1:
        print(element)
    
    

    
    

if __name__ == "__main__":
    main()