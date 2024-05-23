#csvPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/01_exe9_data.csv"
csvPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/01_exe9_data.csv"

with open(csvPath,"r") as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    lineSplit = line.split(",")
    if lineSplit[0].isdigit():
        firstnumber = float(lineSplit[0])
        secondnumber = float(lineSplit[1])
        if 0<secondnumber<1000:
            print(line)
 
    
