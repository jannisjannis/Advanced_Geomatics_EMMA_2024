#txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"


Staname = {'ID': [], 'Name':[], 'Cn':[], 'Lat':[], 'Lon':[], 'Hght':[]}
count = 0
with open(txtPath,"r") as file:
    next(file)
    for line in file:
        ID, Name, Cn, Lat, Lon, Hght = line.strip().split(',')
        Staname['Name'].append(Name)
        count += 1
print(count)