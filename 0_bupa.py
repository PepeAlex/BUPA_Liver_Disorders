import pandas as pd

# extracting BUPA data and adding names to it.
names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks Numbers','Field']
BUPA = pd.read_csv(("bupa.csv"), names=names)

print(BUPA)