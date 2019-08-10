import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

# set the boxplot graph for BUPA
plt.figure(figsize = (10, 8)) # set the graph size
plt.title("BUPA dataset variables") # title of the plot

# set the boxplot style
sns.set(style="darkgrid", color_codes=True) # set the background colour
sns.boxplot(data=BUPA) # set the dataset to plot

# plot the data
plt.show()