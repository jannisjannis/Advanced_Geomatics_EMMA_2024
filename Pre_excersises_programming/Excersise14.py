#txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"


with open(txtPath,"r") as file:
    for i, line in enumerate(file):
        if i == 20:
            break
        print(line.strip())