import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# set the backround colur of the histogram graph
sns.set(style="whitegrid")

# set the bar colour, figure size and bin size of the graphs
BUPA.hist(color = "red", figsize = (12, 8), bins = 18)
# plot the graph
plt.show()