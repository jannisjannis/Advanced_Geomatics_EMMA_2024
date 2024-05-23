#txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"


Staname = {'ID': [], 'Name':[], 'Cn':[], 'Lat':[], 'Lon':[], 'Hght':[]}
with open(txtPath,"r") as file:
    next(file)
    for counter, line in enumerate(file):
        if counter == 20:
            break
        ID, Name, Cn, Lat, Lon, Hght = line.strip().split(',')
        Staname['ID'].append(ID)
        Staname['Name'].append(Name)
        print(f"{Staname['ID'][counter]}. {Staname['Name'][counter].strip()}")
