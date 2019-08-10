import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# set the key parameters for the MCV vs Drinks scatter plot
ax = sns.scatterplot(x="MCV", y="Drinks", hue="Field", data=BUPA)
# set the title of the scatter plot
plt.title("Scatter Plot - 'MCV vs Drinks' of all 2 Fields")
plt.show()

# set the key parameters for the ALKPHOS vs Drinks scatter plot
ax = sns.scatterplot(x="ALKPHOS", y="Drinks", hue="Field", data=BUPA)
# set the title of the scatter plot
plt.title("Scatter Plot - 'ALKPHOS vs Drinks' of all 2 Fields")
plt.show()

# set the key parameters for the SGPT vs Drinks scatter plot
ax = sns.scatterplot(x="SGPT", y="Drinks", hue="Field", data=BUPA)
# set the title of the scatter plot
plt.title("Scatter Plot - 'SGPT vs Drinks' of all 2 Fields")
plt.show()

# set the key parameters for the SGOT vs Drinks scatter plot
ax = sns.scatterplot(x="SGOT", y="Drinks", hue="Field", data=BUPA)
# set the title of the scatter plot
plt.title("Scatter Plot - 'SGOT vs Drinks' of all 2 Fields")
plt.show()

# set the key parameters for the GAMMAGT vs Drinks scatter plot
ax = sns.scatterplot(x="GAMMAGT", y="Drinks", hue="Field", data=BUPA)
# set the title of the scatter plot
plt.title("Scatter Plot - 'GAMMAGT vs Drinks' of all 2 Fields")
plt.show()
