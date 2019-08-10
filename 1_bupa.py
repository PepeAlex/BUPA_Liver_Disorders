import pandas as pd

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks Numbers','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

print("-" * 38)
print(str(BUPA.info())) # information about the dataset
print("-" * 93)
print(str(BUPA.describe())) # summary of each variables
print("-" * 93)
print()
print(str(BUPA.shape) + "\n") # total row and column count
print("-" * 59)
print(str(BUPA.head()) + "\n") # print first 5 rows
print("-" * 61)
print(str(BUPA.tail()) + "\n") # print last 5 rows
print("-" * 61)
print(str(BUPA.sample(10)) + "\n") # output 10 random rows
print("-" * 95)
print((BUPA.columns), "\n") # column names of the dataset
