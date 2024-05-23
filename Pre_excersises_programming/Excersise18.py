#txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"


Staname = {'ID': [], 'Name':[], 'Cn':[], 'Lat':[], 'Lon':[], 'Hght':[]}
Height_total = 0
with open(txtPath,"r") as file:
    next(file)
    for counter, line in enumerate(file):
        ID, Name, Cn, Lat, Lon, Hght = line.strip().split(',')
        Hght = float(Hght)
        Height_total = Height_total + Hght
av_height = Height_total / counter
print(round(av_height, 2))
