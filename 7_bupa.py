import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# set style and background colour using seaborn library
sns.set(style="darkgrid")

sns.distplot(BUPA["MCV"], color= "green")
plt.title('Histogram - MCV of All Data')
plt.xlabel('MCV')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["ALKPHOS"], color= "blue")
plt.title('Histogram - Alkphos of All Data')
plt.xlabel('Alkphos')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["SGPT"], color= "orange")
plt.title('Histogram - SGPT of All Data')
plt.xlabel('SGPT')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["SGOT"], color= "red")
plt.title('Histogram - SGOT of All Data')
plt.xlabel('SGOT')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["GAMMAGT"], color= "pink")
plt.title('Histogram - GammaGT of All Data')
plt.xlabel('GammaGT')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["Drinks"], color= "purple")
plt.title('Histogram - Drinks of All Data')
plt.xlabel('Drinks')
plt.ylabel('count')
plt.show()

sns.distplot(BUPA["Field"], color= "yellow")
plt.title('Histogram - Field of All Data')
plt.xlabel('Field')
plt.ylabel('count')
plt.show()