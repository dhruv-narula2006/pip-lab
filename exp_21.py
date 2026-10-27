'''21. Write a Python Script to read and analyze a CSV or Excel file containing two columns using Pandas and visualize the data using Matplotlib.'''

import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter the name of the file (with extension .csv or .xlsx): ")  

# Read the csv or excel file
if file.endswith(".csv"):
    df = pd.read_csv(file)
else:
    df = pd.read_excel(file)

# Use the first two columns and drop the missing values
df = df.iloc[:, :2].dropna()
x_col, y_col = df.columns

# Analyze the data
print(df.head(), "\n")
print(df.describe(), "\n")
print("Correlation: ", df[x_col].corr(df[y_col]))

# Visualize
plt.figure(figsize=(8,5))
plt.plot(df[x_col], df[y_col], marker="o")
plt.title(f"{y_col} vs {x_col}")
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.grid(True)
plt.show()