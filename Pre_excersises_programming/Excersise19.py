txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
# txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/stations.txt"


Staname = {'ID': [], 'Name':[], 'Cn':[], 'Lat':[], 'Lon':[], 'Hght':[]}
headers = []
Height_total = 0
count = 0
with open(txtPath,"r") as file:
    next(file)
    for counter, line in enumerate(file):
        ID, Name, Cn, Lat, Lon, Hght = line.strip().split(',')
        Hght = float(Hght)
        Height_total = Height_total + Hght
        Staname['Name'].append(Name)
        count += 1
av_height = Height_total / counter


print(f"File info: station.txt\n --------------------- \nStations count: {count}\nAverage value: {round(av_height, 2)}")
print(f"Available fields:")
for key, value in enumerate(Staname):
    headers.append(value)
    print(f" -> {headers[key]}")
print(f"\nFirst data lines:")

StanameX = {'ID': [], 'Name':[], 'Cn':[], 'Lat':[], 'Lon':[], 'Hght':[]}
with open(txtPath,"r") as filex:
    for counter, line in enumerate(filex):
        if counter == 4:
            break
        ID, Name, Cn, Lat, Lon, Hght = line.strip().split(',')
        StanameX['ID'].append(ID)
        StanameX['Name'].append(Name)
        StanameX['Cn'].append(Cn)
        StanameX['Lat'].append(Lat)
        StanameX['Lon'].append(Lon)
        StanameX['Hght'].append(Hght)
        print(f"{StanameX['ID'][counter]}. {StanameX['Name'][counter]}, {StanameX['Cn'][counter]},{StanameX['Lat'][counter]}, {StanameX['Lon'][counter]}, {StanameX['Hght'][counter]}")
