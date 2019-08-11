# BUPA Liver Disorders data set - Project
## Project 2019
### Institution: Galway-Mayo Institute of Technology - GMIT 
### Course: Higher Diploma in Data Analytics
### Module: Programming & Scripting - 1º sem/2019
### Author: Alexander Pepe

> This repository is a research about the BUPA dataset and its importance. I wrote some Python codes to demonstrate more easily and more didactically this dataset and finally summarise it with our findings and conclusion.. This project is part of the discipline of Programming & Scripting the semester end at GMIT.


> This project is avaiable on https://github.com/PepeAlex/BUPA_Project . If you want to try it as Programer, you will need to install some of programms and your libraries.

# INTRODUCTION

   Your liver is an important organ that performs hundreds of tasks related to metabolism, energy storage, and detoxification of waste. It helps you digest food, convert it to energy, and store the energy until you need it. It also helps filter toxic substances out of your bloodstream.
   
   Liver disease is a general term that refers to any condition affecting your liver. These conditions may develop for different reasons, but they can all damage your liver and impact its function. https://www.healthline.com/health/what-does-the-liver-do .
   
## WHAT ARE SOME COMMON LIVER PROBLEMS?

Many conditions can affect your liver. Here is a look at some of the main ones.

- ### Hepatitis
Hepatitis is a viral infection of your liver. It causes inflammation and liver damage, making it difficult for your liver to function as it should. 

- ### Fatty liver disease
Fatty liver is also known as hepatic steatosis. It happens when fat builds up in the liver. Having small amounts of fat in your liver is normal, but too much can become a health problem. One of the primary causes is too much Alcoholic.

- ### Autoimmune Conditions
Autoimmune conditions involve your immune system mistakenly attacking healthy cells in your body. 

https://www.healthline.com/health/liver-diseases

## Liver desease aspect:
![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/liver.png)
https://theceliacscene.com/hepatic-manifestations-celiac-disease/

# BUPA

BUPA Liver Disorders dataset was created by BUPA Medical Research Ltd in May fifteenth of nineteen ninety and the heard of this project was Richard S. Forsyth. This project collected samples of 345 male patients and were analysing 7 variables being 5 in blood tests 1 of drinks numbers por day and 1 field, created by BUPA researchers. https://www.openml.org/d/8

### Variables information:
1- MCV - _Mean Corpuscular Volume_. An MCV blood test measures the average size of your red blood cells, also known as erythrocytes. https://medlineplus.gov/lab-tests/mcv-mean-corpuscular-volume/

2- ALKPHOS – _Alkaline Phosphatase_ (ALP) is an enzyme found in several tissues throughout the body. The highest concentrations of ALP are present in the cells that comprise bone and the liver. https://labtestsonline.org/tests/alkaline-phosphatase-alp#

3- SGTP - _Sérum glutamic pyruvic transaminase_. An enzyme that is normally present in liver and heart cells. SGPT is released into blood when the liver or heart are damaged. https://www.rxlist.com/script/main/art.asp?articlekey=6321

4- SGOT - _Sérum glutamic oxaloacetic transaminase_. An enzyme that is normally present in liver and heart cells. SGOT is released into blood when the liver or heart is damaged. https://www.rxlist.com/script/main/art.asp?articlekey=6320

5- Gamma GT - _glutamytransferase_. An enzyme found in liver cells and the biliary tract. It is a very sensitive indicator of abnormality in the liver or bile duct system. http://www.irishhealth.com/askdoc.html?q=6201

6- _DRINKS_ - number of half-pint equivalents of alcoholic beverages drunk per day. https://www.openml.org/d/8

7- _FIELD_ - selector field created by the BUPA researchers to split the data into train/test sets. https://www.openml.org/d/8

# DESCRIPTION
To complete this project I used some programmes and their libraries. Below is described a little of each of them.

### PYTHON
- Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. https://www.python.org/doc/essays/blurb/
   - Python Libraries:
      - Matplotlib: is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits. https://matplotlib.org/
      - Pandas: is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a world-class open-source project, and makes it possible to donate to the project. https://pandas.pydata.org/
      - 	Seaborn: is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. https://seaborn.pydata.org/
### CMDER
CMDER is a software package created out of pure frustration over the absence of nice console emulators on Windows. It is based on amazing software, and spiced up with the Monokai color scheme and a custom prompt layout, looking sexy from the start.
https://cmder.net/
### VSCODE
Visual Studio Code – VSCode is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring. https://en.wikipedia.org/wiki/Visual_Studio_Code  https://code.visualstudio.com/
### CSV File - Data Set https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/

# Analysing
> Firstly I downloaded the BUPA dataset from the website: https://archive.ics.uci.edu/ml/machine-learning-databases/liver-disorders/ ; and saved this file as "bupa.csv" in my computer. I opened the VSCode and I created a file called 0_bupa.py. I imported pandas library as "pd" and added column names to the data then I wrote a code _BUPA= pd.read_csv(("bupa.csv")_, names=names). See below:

      import pandas as pd
      # extracting BUPA data and adding names to it.
      names = ['MCV','ALKPHOS','SGPT','SGOT','GAMMAGT','Drinks Numbers','Field']
      BUPA = pd.read_csv(("bupa.csv"), names=names)

      print(BUPA)

> Below I wrote some Python Script about BUPA Liver Dataset in brief:

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
      
> This is the result of my code and contains a general brief respectively:

1. _BUPA Information_ contain names and numbers of variables, numbers of samples, datatype used in each column and memory usage.

2. _Description_, there are statistical summary as count variables, mean, standard deviation, 25%th, 50%th and 75%th on each column.

3.  _Shape_, total numbers of columns and rows in this dataset.

4. _Head_, list  the top 5 rows of the data.

5. _Tail_, list the lat 5 rows of the data.

6. _Sample_, list randow 10 rows of the data.

7. _Column_, column names of the data.

![Alt text](https://github.com/PepeAlex/BUPA_Project/blob/writing/1_bupa.png)

# Statistic

> In this part of my project I wrote some Python Scripts to show how to manupulate the data using "pandas library". I used "loc function" to find a "mean" of each variables and for each variables per "Field". Also I used "iloc function" to divide the data in three parts and find the "mean" for each parts. For that I separeted tha data in 0 to 115, 115 to 230 and 230 to 345.

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

> Following the subject I used the data to describe some statistic features as MEAN, MIN, MAX, MEDIAN and MODE, and at least I used it to show each statistic features by each "FIELD".

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
