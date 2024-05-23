#csvPath = "C:/Users/Jannis/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/01_exe11_data.csv"
csvPath = "C:\Users\Jannis\Desktop\JannisReutter_Aufgaben/01_exe11_data.csv"

datadict = {'base': [], 'height':[]}
with open(csvPath,"r") as file:
    for line in file:
        base, height = line.strip().split(';')
        base = base.replace('base=', '')
        base = float(base.replace('cm', ''))
        height = height.replace('height=', '')
        height = float(height)
        datadict['base'].append(base)
        datadict['height'].append(height)

for base,height in zip(datadict['base'], datadict['height']):
    print(f" base * height / 2: {base} * {height*100} = {(base*height*100)/2}cm2.")

