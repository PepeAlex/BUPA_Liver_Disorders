import pandas as pd

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks Numbers','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

print("Mean of MCV is", BUPA["MCV"].mean())
print("Mean of Alkphos is", BUPA["ALKPHOS"].mean())
print("Mean of SGTP is", BUPA["SGPT"].mean())
print("Mean of SGOT is", BUPA["SGOT"].mean())
print("Mean of GAMMAGT is", BUPA["GAMMAGT"].mean())
print("Mean of Drinks Numbers is", BUPA["Drinks Numbers"].mean())
print("\n")

group = BUPA.groupby("Field")

print("Mean of all 2 Field")
print(group.mean())
print("\n")

print("Finding mean of Fields using 'loc' function", "\n")
print("Mean of Field 1")
print(BUPA.loc[BUPA["Field"]== 1].mean())  # mean of Field 1 using loc function
print("\n")
print("Mean of Field 2")
print(BUPA.loc[BUPA["Field"]== 2].mean()) # mean of Field 2 using loc function
print("\n")

print("Finding mean of species using 'iloc' function", "\n")
print("Mean of Variances")
print(BUPA.iloc[0:115].mean()) # mean of variables using iloc function
print("\n")
print("Mean of Variances")
print(BUPA.iloc[115:230].mean()) # mean of variables using iloc function
print("\n")
print("Mean of Variances")
print(BUPA.iloc[230:345].mean()) # mean of variables using iloc function