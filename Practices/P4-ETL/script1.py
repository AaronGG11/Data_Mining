import os
import csv
import datetime
import pandas as pd 
'''
    SCRIPT FOR CLEANING, TRANSFORMING AND VALIDATE THE DATA
'''


def main():
    # creating a dictionary containing a date
    dict = {'Date':["2020-06-17", "2020-01-14", 
                    "2020-09-20", "2020-08-15"]}
    
    # converting the dictionary to a 
    # dataframe
    df = pd.DataFrame.from_dict(dict)
    
    # converting the date to the required 
    # format
    df['Date'] = pd.to_datetime(df['Date'],
                                errors ='coerce')
    df.astype('int64').dtypes
    
    # extracting the week from the date
    weekNumber = df['Date'].dt.week
    
    print(weekNumber)

if __name__ == "__main__":
    main()