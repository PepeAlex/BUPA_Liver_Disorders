import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# boxplot MCV vs Drinks
sns.boxplot(x="Drinks", y="MCV", data=BUPA)
plt.show()

# boxplot ALKPHOS vs Drinks
sns.boxplot(x="Drinks", y="ALKPHOS", data=BUPA)
plt.show()

# boxplot SGPT vs Drinks
sns.boxplot(x="Drinks", y="SGPT", data=BUPA)
plt.show()

# boxplot SGOT vs Drinks
sns.boxplot(x="Drinks", y="SGOT", data=BUPA)
plt.show()

# boxplot GAMMAGT vs Drinks
sns.boxplot(x="Drinks", y="GAMMAGT", data=BUPA)
plt.show()
