# BUPA Liver Disorders data set - Project
## Project 2019
### Institution: Galway-Mayo Institute of Technology - GMIT 
### Course: Higher Diploma in Data Analytics
### Module: Programming & Scripting - 1º sem/2019
### Author: Alexander Pepe

> This paper is research about the BUPA Liver Disorders dataset and its importance. I have written some Python codes to demonstrate this dataset more easily and more didactically. Finally, I will summarise my findings and present my conclusion. This project is part of the semester end requirement in the discipline of Programming & Scripting at GMIT.


> This project is avaiable at https://github.com/PepeAlex/BUPA_Project. In order to try it as a programer, some programms and libraries will need to be installed.

# INTRODUCTION

The liver is an important organ that performs hundreds of tasks related to metabolism, energy storage, and detoxification of waste. It helps to digest food, convert it to energy, and store the energy until needed. It also helps to filter toxic substances out of the bloodstream.
   
Liver disease is a general term that refers to any condition affecting the liver. These conditions may develop for different reasons, but they can all damage the liver and impact its function. https://www.healthline.com/health/what-does-the-liver-do .
   
## WHAT ARE SOME COMMON LIVER PROBLEMS?

Many conditions can affect the liver. Here is a summary of some of the main ones.

- ### Hepatitis
Hepatitis is a viral infection of the liver. It causes inflammation and liver damage, making it difficult for the liver to function as it should. 

- ### Fatty liver disease
Fatty liver is also known as hepatic steatosis. It happens when fat builds up in the liver. Having small amounts of fat in the liver is normal, but too much can become a health problemç one of the primary causes is too much alcohol.

- ### Autoimmune Conditions
Autoimmune conditions involve the immune system mistakenly attacking healthy cells in the body. 

https://www.healthline.com/health/liver-diseases

## Liver disease aspect:
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/liver.png)
https://theceliacscene.com/hepatic-manifestations-celiac-disease/

# BUPA

The BUPA Liver Disorders dataset was created by BUPA Medical Research Ltd on May 15, 1990ç the heard of this project was Richard S. Forsyth. This project collected samples of 345 male patients and analysed seven variables created by BUPA researchers: five "blood" (blood tests), one "drinks" (number of drinks per day), and one "field" (train versus test results) . https://www.openml.org/d/8

### Variables information:
1- MCV - _Mean Corpuscular Volume_. An MCV blood test measures the average size of red blood cells, also known as erythrocytes. https://medlineplus.gov/lab-tests/mcv-mean-corpuscular-volume/

2- ALKPHOS – _Alkaline Phosphatase_ (ALP) is an enzyme found in several tissues throughout the body. The highest concentrations of ALP are present in the cells that comprise bone and the liver. https://labtestsonline.org/tests/alkaline-phosphatase-alp#

3- SGTP - _Sérum glutamic pyruvic transaminase_. An enzyme that is normally present in liver and heart cells. SGPT is released into the blood when the liver or heart is damaged. https://www.rxlist.com/script/main/art.asp?articlekey=6321

4- SGOT - _Sérum glutamic oxaloacetic transaminase_. An enzyme that is normally present in liver and heart cells, SGOT is released into the blood when the liver or heart is damaged. https://www.rxlist.com/script/main/art.asp?articlekey=6320

5- Gamma GT - _glutamytransferase_. An enzyme found in liver cells and the biliary tract, it is a very sensitive indicator of abnormality in the liver or bile duct system. http://www.irishhealth.com/askdoc.html?q=6201

6- _DRINKS_ - number of half-pint equivalents of alcoholic beverages drunk per day. https://www.openml.org/d/8

7- _FIELD_ - selector field created by the BUPA researchers to split the data into train/test sets. https://www.openml.org/d/8

# DESCRIPTION
To complete this project, I have used some programmes and their libraries; below is a short description of each.

### PYTHON
- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level, built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for rapid application development, as well as for use as a scripting or glue language to connect existing components together. https://www.python.org/doc/essays/blurb/
   - Python Libraries:
      - Matplotlib: is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, Python and IPython shells, Jupyter notebook, web application servers, and four graphical user interface toolkits. https://matplotlib.org/
      - Pandas: is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a world-class open-source project, and makes it possible to donate to the project. https://pandas.pydata.org/
      - Seaborn: is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. https://seaborn.pydata.org/
### CMDER
CMDER is a software package created out of the absence of suitable console emulators in Windows. It is based on quality software, with a Monokai color scheme and a custom prompt layout.
https://cmder.net/
### VSCODE
Visual Studio Code – VSCode is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. https://en.wikipedia.org/wiki/Visual_Studio_Code  https://code.visualstudio.com/
### CSV File - Data Set 
https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/
### GITHUB
GitHub is a Git repository hosting service, but it adds many of its own features; while Git is a command line tool, GitHub provides a Web-based graphical interface. It also provides access control and several collaboration features, such as a wikis and basic task management tools for every project. https://techcrunch.com/2012/07/14/what-exactly-is-github-anyway/?guccounter=1&guce_referrer_us=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_cs=QdRUp8Vpgm9JNIVT4qpoSA

# Analysing
> Firstly, I downloaded the BUPA dataset from the website: https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/ ; and saved this file as "bupa.csv" on my computer. I opened the VSCode and created a file called 0_bupa.py. I imported the pandas library as "pd" and added column names to the data; then I wrote a code _BUPA= pd.read_csv(("bupa.csv")_, names=names). See below:

      import pandas as pd
      # extracting BUPA data and adding names to it.
      names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks Numbers','Field']
      BUPA = pd.read_csv(("bupa.csv"), names=names)

      print(BUPA)

> Below, I wrote some Python Script about the BUPA Liver Dataset. In brief:

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
      
> This is the result of my code and contains a general brief. Respectively:

1. _BUPA Information_ contain names and numbers of variables, numbers of samples, datatype used in each column and memory usage.

2. _Description_, there are statistical summary as count variables, mean, standard deviation, 25%th, 50%th and 75%th on each column.

3.  _Shape_, total numbers of columns and rows in this dataset.

4. _Head_, list  the top 5 rows of the data.

5. _Tail_, list the lat 5 rows of the data.

6. _Sample_, list randow 10 rows of the data.

7. _Column_, column names of the data.

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/1_bupa.png)

# Statistic

> In this part of my project, I wrote some Python Scripts to show how to manupulate the data using pandas library. I used "loc function" to find a "mean" of each variables and for each variable per "Field". Also I used "iloc function" to divide the data into three parts and find the "mean" for each parts. For that, I separeted tha data into 0 to 115, 115 to 230 and 230 to 345 samples.

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

      print("Finding mean of variables using 'iloc' function", "\n")
      print("Mean of Variances")
      print(BUPA.iloc[0:115].mean()) # mean of variables using iloc function
      print("\n")
      print("Mean of Variances")
      print(BUPA.iloc[115:230].mean()) # mean of variables using iloc function
      print("\n")
      print("Mean of Variances")
      print(BUPA.iloc[230:345].mean()) # mean of variables using iloc function

> Above is the result by CMDER

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/2_bupa.png)

> Following the subject, I used the data to describe some statistical features such as MEAN, MIN, MAX, MEDIAN and MODE, and lastly, I used it to show each statistic features by each "FIELD".

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

> The result by CMDER:
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/3_bupa.png)

> One more type of statistic utilized was "pivot function". It is exceedingly useful, and uses the syntax to format the output needed. In this code, I described each column divided by "Field" and listed the count in each "Field", the mean, the standard deviation, MIN, MAX, and 25%th, 50%th and 75%th percentiles' of each numeric columns.
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

> This code produced the follwing answers:

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/4_bupa.png)

# Graphic

> In this section of my project, I built some graphics to easily describe my BUPA Dataset, and for that I used pandas, matplolib and seaborn libraries. The first graphic is a general visualization of the data.

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
 
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/5_bupa.png)
   
> Then I decided to show the relation betwen numbers of "Drinks" versus each variable of blood test.

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

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/6_bupa_MCV.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/6_bupa_ALPHOS.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/6_bupa_SGPT.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/6_bupa_SGOT.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/6_bupa_GAMMAGT.png)
 
 > I also used the HISTOGRAM graphic type to illustrate my data.
 
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

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_MCV.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_ALPHOS.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_SGPT.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_SGOT.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_GAMMAGT.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_Drinks.png)
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/7_bupa_field.png)

> I presented one more HISTOGRAM, but now they were together in the same code.

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

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/8_bupa.png)

> Finally, I manipulated my data and used SCATTER PLOT to show it per numbers of field and "Drinks" versus blood variable.

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
      
 ![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/9_bupa_MCV.png)
 ![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/9_bupa_ALPHOS.png)
 ![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/9_bupa_SGPT.png)
 ![Alt tet](https://github.com/PepeAlex/BUPA_Project/blob/writing/9_bupa_SGOT.png)
 ![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/9_bupa_GAMMAGT.png)
 
# Conclusion
 
The BUPA Liver Dissorders Dataset is research that uses blood variables to demontrate liver disorders. I found some projects on this in data science, but all of these projects are at an early stage and I have not seen much information. In my project, I tried to use all the knowledge imparted in the first semester of the "Programming & Scripts" subject at GMIT.

Some of the libraries of Python such as "PANDAS", "MATPLOTLIB" and "SEABORN" are widely used in this project. PANDAS is a good tool to work with labels; MATPLOTLIB and SEABORN are good tools to work with graphics and charts. I downloaded the data and saved it in a CSV type file and I used these libraries to extract it.

For me, this project was a challenge because every subject in IT was new, and I had to pay close attention because my previous degree had been in science, where my focus was not on blood variables, but on how to manipulate and illustrate data. I learnt each IT subject separately and after that, assimilated everything to finalize and make my presentation on the GITHub site. For this project, I needed to understand the dataset, how to manipulate it, and which type of graphics to choose.
 
# References

1. Liver Introduction - https://www.healthline.com/health/what-does-the-liver-do
2. Liver Problems - https://www.healthline.com/health/liver-diseases
3. Liver Disease picture - https://theceliacscene.com/hepatic-manifestations-celiac-disease/
4. BUPA Dataset definition - https://www.openml.org/d/8
5. MCV definition -  https://medlineplus.gov/lab-tests/mcv-mean-corpuscular-volume/
6. ALKPHOS definition - https://labtestsonline.org/tests/alkaline-phosphatase-alp#
7. SGPT definition - https://www.rxlist.com/script/main/art.asp?articlekey=6321
8. SGOT definition -  https://www.rxlist.com/script/main/art.asp?articlekey=6320 
9. GAMMAGT definition - http://www.irishhealth.com/askdoc.html?q=6201 
10. Drinks definition -  https://www.openml.org/d/8
11. Field definition - https://www.openml.org/d/8
12. Python - https://www.python.org/doc/essays/blurb/
13. Matplotlib - https://matplotlib.org/
14. Pandas - https://pandas.pydata.org/
15. Seaborn -  https://seaborn.pydata.org/
16. CMDER -  https://cmder.net/
17. VSCODE -  https://en.wikipedia.org/wiki/Visual_Studio_Code https://code.visualstudio.com/
18. BUPA Dataset -  https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/
19. GITHUB - https://techcrunch.com/2012/07/14/what-exactly-is-github-anyway/?guccounter=1&guce_referrer_us=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_cs=QdRUp8Vpgm9JNIVT4qpoSA
