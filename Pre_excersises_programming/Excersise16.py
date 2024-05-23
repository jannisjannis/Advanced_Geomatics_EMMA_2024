#txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"

with open(txtPath,"r") as file:
    first_line = file.readline()
    columns = len(first_line.strip().split(','))
print(columns)