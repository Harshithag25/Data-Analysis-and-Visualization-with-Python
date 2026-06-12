#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df=pd.read_csv("data.csv")
df=df[['Order Date','Customer ID','Segment','Region','Category','Sales','Quantity','Profit']]
print("Dataset Preview: ")
print(df.head())

df['Order Date']=pd.to_datetime(df['Order Date'])  #convert order date to datetime.
df=df.dropna()
print("Cleaned Dataset Info: ")
print(df.info()) 

#Basic Analysis
print("\n Summary Statistics: ")
print(df.describe())
print("Average Sales:", round(df['Sales'].mean(),2))
print("\n Average Profit by Category: ")
print(df.groupby('Category')['Profit'].mean()) 