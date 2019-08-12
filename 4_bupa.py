import pandas as pd

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# pivoting the dataset with describe method based on the variable column
print("Pivot the dataframe based on the values in the 'MCV' column", "\n")
print(BUPA.pivot(columns='Field', values='MCV').describe(), "\n")
print("Pivot the dataframe based on the values in the 'Alkphos' column", "\n")
print(BUPA.pivot(columns='Field', values='ALKPHOS').describe(), "\n")
print("Pivot the dataframe based on the values in the 'SGPT' column", "\n")
print(BUPA.pivot(columns='Field', values='SGPT').describe(), "\n")
print("Pivot the dataframe based on the values in the 'SGOT' column", "\n")
print(BUPA.pivot(columns='Field', values='SGOT').describe(), "\n")
print("Pivot the dataframe based on the values in the 'GammaGT' column", "\n")
print(BUPA.pivot(columns='Field', values='GAMMAGT').describe(), "\n")
print("Pivot the dataframe based on the values in the 'Drinks' column", "\n")
print(BUPA.pivot(columns='Field', values='Drinks').describe(), "\n")
print("Pivot the dataframe based on the values in the 'Field' column", "\n")
print(BUPA.pivot(columns='Field', values='Field').describe(), "\n")

# describe entire dataset for all Field
print("Describe the entire dataframe", "\n")
print(BUPA.describe(), "\n")