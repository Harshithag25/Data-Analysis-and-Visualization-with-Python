#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset
df=pd.read_csv("data.csv" , encoding="latin1")
df=df[['Row ID','Order Date','Customer ID','Segment','Region','Category','Sales','Quantity','Profit']]
print("Dataset Preview: ")
print(df['Order Date'].head())

df['Order Date']=pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')  #convert order date to datetime.
df=df.dropna()
print("Cleaned Dataset Info: ")
print(df.info()) 

#Basic Analysis
print("\n Summary Statistics: ")
print(df.describe())
print("Average Sales:", round(df['Sales'].mean(),2))
print("\n Average Profit by Category: ")
print(df.groupby('Category')['Profit'].mean()) 

#Bar Chart
sales_by_category = df.groupby('Category')['Sales'].sum()
sales_by_category.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category') 
plt.ylabel('Sales')
plt.savefig('bar_chart.png')
plt.show() 

#Scatter Plot
sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', color='red') 
plt.title('Sales Vs Profit by Category')
plt.savefig('scatter_plot.png') 
plt.show() 

#Heatmap
corr = df[['Sales','Quantity','Profit']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap (Sales, Quantity, Profit)')
plt.savefig("heatmap.png")
plt.show()

#Linechart
sales_trend = df.groupby('Order Date')['Sales'].sum().reset_index()
sns.lineplot(x='Order Date', y='Sales', data=sales_trend, marker='o')
plt.title('Sales Trend Over Time')
plt.xlabel('Order Date')
plt.ylabel('Total Sales')
plt.savefig("linechart.png")
plt.show()