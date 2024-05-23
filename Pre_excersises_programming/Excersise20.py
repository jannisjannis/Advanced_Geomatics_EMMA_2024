txtPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/station_data.txt"
# txtPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/station_data.txt"


Staname = {'ID': [], 'Squid':[], 'Date':[], 'RR':[], 'Q_RR':[]}
headers = []
RR_total = 0
count = 0
with open(txtPath,"r") as file:
    next(file)
    for counter, line in enumerate(file):
        ID, Squid, Date, RR, Q_RR = line.strip().split(',')
        RR = float(RR)
        if RR >= 0:
            RR_total = RR_total + RR
            Staname['ID'].append(ID)
            count += 1
av_RR = RR_total / counter


print(f"File info: station_data.txt\n --------------------- \nStations count: {count}\nAverage value: {round(av_RR, 2)}")
print(f"Available fields:")
for key, value in enumerate(Staname):
    headers.append(value)
    print(f" -> {headers[key]}")
print(f"\nFirst data lines:")

StanameX = {'ID': [], 'Squid':[], 'Date':[], 'RR':[], 'Q_RR':[]}
with open(txtPath,"r") as filex:
    for counter, line in enumerate(filex):
        if counter == 8:
            break
        ID, Squid, Date, RR, Q_RR = line.strip().split(',')
        StanameX['ID'].append(ID)
        StanameX['Squid'].append(Squid)
        StanameX['Date'].append(Date)
        StanameX['RR'].append(RR)
        StanameX['Q_RR'].append(Q_RR)
        print(f"{StanameX['ID'][counter]}. {StanameX['Squid'][counter]}, {StanameX['Date'][counter]},{StanameX['RR'][counter]}, {StanameX['Q_RR'][counter]}")
