import math
import matplotlib.pyplot as plt
import random
import numpy as np

def generate_data(max_value, length):
    return [((random.random()*2)-1)*max_value for _ in range(length)]
    
def generate_data_lisse(max_value, length):
    t = np.linspace(-np.pi, np.pi, length)
    raw = np.sin(t) + 0.5*np.cos(2*t)
    raw_min, raw_max = np.min(raw), np.max(raw)
    norm = 2*(raw - raw_min) / (raw_max - raw_min) - 1
    data = norm * max_value
    return data

def uneDecomposition(data):
    new_data = []
    coeff = []
    for i in range(0, len(data)-1, 2):
        moyenne = (data[i]+data[i+1])/2
        new_data.append(moyenne)
        coeff.append(data[i]-moyenne)
    return new_data,coeff

def uneRecomposition(data, coeff):
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i] + coeff[i])
        new_data.append(data[i] - coeff[i])
    return new_data

def Decomposition(data):
    new_data = data
    coeff = []
    while len(new_data) > 1:
        new_data,new_coeff = uneDecomposition(new_data)
        coeff.insert(0, new_coeff)
    return new_data,coeff

def Recomposition(data, coeff):
    new_data = data
    for current_coeff in coeff:
        new_data = uneRecomposition(new_data, current_coeff)
    return new_data

def RemoveSmallCoeff(coeff, seuil):
    return [c if abs(c) > seuil else 0.0 for c in coeff]

def GlobalRemoveSmallCoeff(coeff, seuil):
    return [RemoveSmallCoeff(c,seuil) for c in coeff]

def RecompositionRemoveSmallCoeff(data, coeff, seuil):
    new_coeff = GlobalRemoveSmallCoeff(coeff, seuil)
    return Recomposition(data, new_coeff)

def Error1(data, seuil):
    decomposition,coeff = Decomposition(data)
    new_data = RecompositionRemoveSmallCoeff(decomposition, coeff, seuil)
    sum = 0
    for i in range(len(data)):
    	sum += abs(data[i] - new_data[i])
    return sum/len(data)
    
def Error2(data, seuil):
    decomposition,coeff = Decomposition(data)
    new_data = RecompositionRemoveSmallCoeff(decomposition, coeff, seuil)
    sum = 0
    for i in range(len(data)):
    	sum += (data[i] - new_data[i])**2
    return (math.sqrt(sum))/len(data)

def histo(data, seuil):
    new_data,coeff = Decomposition(data)
    abs_coeff = [abs(c) for current_coeff in coeff for c in current_coeff]
    coeff_min = int(min(abs_coeff))
    coeff_max = int(max(abs_coeff))
    bins = range(coeff_min, coeff_max + 2)
    plt.figure(figsize=(6,4))
    plt.hist(abs_coeff, bins=bins, color='skyblue', edgecolor='black')
    plt.title("Répartition des valeurs absolues des coefficients de détails")
    plt.xlabel("coefficient de détail")
    plt.ylabel("nombre d'occurences")
    plt.axvline(x=seuil, linestyle='--', linewidth=2, color='red')
    plt.grid(True, linestyle='--', alpha=1)

def graphError1(data):
    new_data,coeff = Decomposition(data)
    abs_coeff = [abs(c) for current_coeff in coeff for c in current_coeff]
    seuil_max = max(abs_coeff)
    step = seuil_max/100
    res = []
    for i in np.arange(0,seuil_max,step):
    	res.append([i,Error1(data,i)])
    x = [pair[0] for pair in res]
    y = [pair[1] for pair in res]
    plt.figure(figsize=(6,4))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', label='data')
    plt.title("Erreur en fonction du seuil de mise à zéro des coefficients de détails")
    plt.xlabel("seuil")
    plt.ylabel("erreur")
    plt.show()

def behavior(max_value, length, seuil):
    # données irrégulières
    x = np.arange(length)
    
    data1 = generate_data(max_value, length)
    new_data1, coeff1 = Decomposition(data1)
    new_data2 = RecompositionRemoveSmallCoeff(new_data1, coeff1, seuil)

    plt.figure(figsize=(6,8))
    plt.subplot(2,1,1)
    plt.plot(x, data1, label="données originales")
    plt.plot(x, new_data2, label="données reconstruites")
    plt.title("Comportement sur des données irrégulières")
    plt.legend()
    plt.grid(True)

    # données lisses
    data2 = generate_data_lisse(max_value, length)
    new_data3, coeff2 = Decomposition(data2)
    new_data4 = RecompositionRemoveSmallCoeff(new_data3, coeff2, seuil)
    
    plt.subplot(2,1,2)
    plt.plot(x,data2, label="données originales")
    plt.plot(x, new_data4, label="données reconstruites")
    plt.title("Comportement sur des données lisses")
    plt.legend()
    plt.grid(True)
    plt.show()

#-----------------------------------------------------------------
max_value = int(input("Valeur max des données : "))
length = int(input("Nombre de données : "))
data = generate_data(max_value, length)
seuil = float(input("Valeur seuil : "))
print("Initial data : ")
print(data)
data_decomposition,coeff = uneDecomposition(data)
print("One decomposition: ")
print(data_decomposition)
print("Coeff : ")
print(coeff)
data_recomposition = uneRecomposition(data_decomposition, coeff)
print("One recomposition : ")
print(data_recomposition)
print("---------------------------------------------------------")
print("Initial data : ")
print(data)
data_decomposition,coeff = Decomposition(data)
print("Total decomposition : ")
print(data_decomposition)
print("Coeff : ")
print(coeff)
data_recomposition = Recomposition(data_decomposition, coeff)
print("Total Recomposition : ")
print(data_recomposition)
print("---------------------------------------------------------")
print("Initial data : ")
print(data)
data_decomposition,coeff = Decomposition(data)
print("Total decomposition : ")
print(data_decomposition)
print("Coeff : ")
print(coeff)
data_recomposition = RecompositionRemoveSmallCoeff(data_decomposition, coeff, seuil)
print("Total recomposition - remove small coeff : ")
print(data_recomposition)
print("---------------------------------------------------------")
print("Error calcul with absolute value :", Error1(data, seuil))
print("Error calcul with square root : ", Error2(data, seuil))
histo(data, seuil)
graphError1(data)
behavior(max_value, length, seuil)
