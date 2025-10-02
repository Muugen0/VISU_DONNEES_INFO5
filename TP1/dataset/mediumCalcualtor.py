import csv

def moyLi(l):
    x = 0
    for i in l :
        x += int(i)
    x = x/len(l)
    return round(x, 2)


with open("TP1/dataset/MentalHealthDataset.csv", newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',')
    
    oldage = -1
    oldgender = -1
    stress = []
    depression = []
    anxiety = []
    risk = []
    
    moyListes = []
    
    for row in spamreader:
        if (row[0] == "age") :
            moyListes.append(row)
            continue
        age = row[0]
        gender = row[1]
        if ((gender != oldgender and oldgender != -1) or (int(age) -3 >= int(oldage) and oldage != -1)) :
            newli = []
            newli.append(str(oldage))
            newli.append(oldgender)
            newli.append(str(moyLi(stress)))
            newli.append(str(moyLi(depression)))
            newli.append(str(moyLi(anxiety)))
            newli.append(str(moyLi(risk)))
            moyListes.append(newli)
            stress = []
            depression = []
            anxiety = []
            risk = []
            oldage = age
        
        stress.append(row[2])
        depression.append(row[3])
        anxiety.append(row[4])
        risk.append(row[5])
        if (oldage == -1):
            oldage = age
        oldgender = gender
        
with open("TP1/dataset/MentalHealthDatasetMoyenne.csv", "w", newline="\n") as file :
    for row in moyListes :
        file.write(','.join(row) + '\n')