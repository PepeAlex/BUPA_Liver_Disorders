import pandas as pd

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

print("Mean of MCV is", BUPA["MCV"].mean())
print("Mean of Alkphos is", BUPA["ALKPHOS"].mean())
print("Mean of SGPT is", BUPA["SGPT"].mean())
print("Mean of SGOT is", BUPA["SGOT"].mean())
print("Mean of GammaGT is", BUPA["GAMMAGT"].mean())
print("Mean of Drinks is", BUPA["Drinks"].mean())
print("Mean of Field is", BUPA["Field"].mean())
print("\n")

# finding the max value of each variable
print("Max value of MCV is", BUPA["MCV"].max())
print("Max value of Alkphos is", BUPA["ALKPHOS"].max())
print("Max value of SGPT is", BUPA["SGPT"].max())
print("Max value of SGOT is", BUPA["SGOT"].max())
print("Max value of GammaGT is", BUPA["GAMMAGT"].max())
print("Max value of Drinks is", BUPA["Drinks"].max())
print("Max value of Field is", BUPA["Field"].max())
print("\n")

# finding the min value of each variable
print("Min value of MCV is", BUPA["MCV"].min())
print("Min value of Alkphos is", BUPA["ALKPHOS"].min())
print("Min value of SGPT is", BUPA["SGPT"].min())
print("Min value of SGOT is", BUPA["SGOT"].min())
print("Min value of GammaGT is", BUPA["GAMMAGT"].min())
print("Min value of Drinks is", BUPA["Drinks"].min())
print("Min value of Field is", BUPA["Field"].min())
print("\n")

# finding the median of each variable
print("Median of MCV is", BUPA["MCV"].median())
print("Median of Alkphos is", BUPA["ALKPHOS"].median())
print("Median of SGPT is", BUPA["SGPT"].median())
print("Median of SGOT is", BUPA["SGOT"].median())
print("Median of GammaGT is", BUPA["GAMMAGT"].median())
print("Median of Drinks is", BUPA["Drinks"].median())
print("Median of Field is", BUPA["Field"].median())
print("\n")

# finding the mode of each variable
print("Mode of MCV is", BUPA["MCV"].mode())
print("\n")
print("Mode of Alkphos is", BUPA["ALKPHOS"].mode())
print("\n")
print("Mode of SGPT is", BUPA["SGPT"].mode())
print("\n")
print("Mode of SGOT is", BUPA["SGOT"].mode())
print("\n")
print("Mode of GammaGT is", BUPA["GAMMAGT"].mode())
print("\n")
print("Mode of Drinks is", BUPA["Drinks"].mode())
print("\n")
print("Mode of Field is", BUPA["Field"].mode())
print("\n")


# group the BUPA dataset by the Field column
group = BUPA.groupby("Field")

# find the mean of each variable for all 2 Field
print("Mean of all 2 Field")
print(group.mean())
print("\n")

# find the max value of each variable for all 2 species
print("Max value of all 2 Field")
print(group.max())
print("\n")

# find the min value of each variable for all 2 species
print("Min value of all 2 Field")
print(group.min())
print("\n")

# find the median of each variable for all 2 species
print("Median of all 2 Field")
print(group.median())
print("\n")