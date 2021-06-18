import os
import csv
import datetime
import pandas as pd 
import numpy as np
from scipy.sparse import data

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score,accuracy_score
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt



def main():    
    path = "../../DataSet/project/TARGET/"
    main_file = "airbnb.csv"
    
    data_x = ["neighbourhood", "room_type", "price", "minimum_nights", "year_data"]
    data_y = "calculated_host_listings_count"
    data = data_x + [data_y]
    
    main_df = pd.read_csv(path + main_file, usecols=data)
    main_df = main_df.astype(float)
    main_df = main_df.head(2000)
    
    df_x = main_df[data_x]
    df_y = main_df[data_y]

    X_train, X_test, y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2)
    
    algoritmo = SVR(kernel="precomputed", C=1.0, epsilon=0.2)
    algoritmo.fit(X_train, y_train)

    
    print(algoritmo.score(X_test, y_test))
    
    






    
    
    
    






if __name__ == "__main__":
    main()