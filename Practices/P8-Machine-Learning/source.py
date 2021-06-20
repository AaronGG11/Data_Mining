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

def removeOutliers(data, low_percentil, high_percentil):
    min_thresold = data.quantile(low_percentil)
    max_thresold = data.quantile(high_percentil)
    
    return (data[data.between(min_thresold, max_thresold)])
    
    


def main():    
    path = "../../DataSet/project/TARGET/"
    main_file = "airbnb.csv"
    
    # Obtener datos de fuente original
    data_x = ["neighbourhood", "room_type", "price", "minimum_nights", "year_data", "availability_365"]
    data_y = "calculated_host_listings_count"
    data = data_x + [data_y]
    
    main_df = pd.read_csv(path + main_file, usecols=data)
    #main_df = main_df.head()
    
    # Eliminar valores atipicos de algunas columnas 
    data_to_put_off_outliers = ['price', 'availability_365','calculated_host_listings_count', 'minimum_nights']
    
    for value in data_to_put_off_outliers:
        main_df[value]  = removeOutliers(main_df[value], 0.05, 0.95)
    
    
    '''
    df_x = main_df[data_x]
    df_y = main_df[data_y]

    X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2)
    '''
    
    

if __name__ == "__main__":
    main()