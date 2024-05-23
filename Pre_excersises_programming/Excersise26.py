#data1 = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/01_exe26_dataset1.csv"
#data2 = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/01_exe26_dataset2.csv"
data1 = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/01_exe26_dataset1.csv"
data2 = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/01_exe26_dataset2.csv"


import pandas as pd

dataframe1 = pd.read_csv(data1)
dataframe2 = pd.read_csv(data2)

merged_dataframe = pd.merge(dataframe1, dataframe2, on='#id', how='inner')

print(merged_dataframe)