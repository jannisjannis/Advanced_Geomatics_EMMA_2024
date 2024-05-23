with open(csvPath,"r") as file:
    lines = file.readlines()
    
for line in lines:
    line = line.strip()
    lineSplit = line.split(",")
    if lineSplit[0].isdigit():
        firstnumber = float(lineSplit[0])
        secondnumber = float(lineSplit[1])
        print(line)