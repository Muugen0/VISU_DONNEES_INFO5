import math
import matplotlib.pyplot as plt
import random

def generate_data(max_value, length):
    return [((random.random()*2)-1)*max_value for _ in range(length)]

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
    print("Coeff after remove small values : ", new_coeff)
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

def histo(coeff, seuil):
    abs_coeff = [c for current_coeff in coeff for c in current_coeff]
    plt.figure(figsize=(6,4))
    plt.hist(abs_coeff, bins='auto', color='skyblue', edgecolor='black')
    plt.title("title")
    plt.xlabel("xlabel")
    plt.ylabel("ylabel")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

#-----------------------------------------------------------------
#data = [9.0,7.0,3.0,5.0,2.0,10.0,8.0,12.0]
data = generate_data(20,256)
seuil = 1.0
print("Initial data : ", data)
data_decomposition,coeff = uneDecomposition(data)
print("One decomposition: ", data_decomposition)
print("Coeff : ", coeff)
data_recomposition = uneRecomposition(data_decomposition, coeff)
print("One recomposition : ", data_recomposition)
print("---------------------------------------------------------")
print("Initial data : ", data)
data_decomposition,coeff = Decomposition(data)
print("Total decomposition : ", data_decomposition)
print("Coeff : ", coeff)
data_recomposition = Recomposition(data_decomposition, coeff)
print("Total Recomposition : ", data_recomposition)
print("---------------------------------------------------------")
print("Initial data : ", data)
data_decomposition,coeff = Decomposition(data)
print("Total decomposition : ", data_decomposition)
print("Coeff : ", coeff)
data_recomposition = RecompositionRemoveSmallCoeff(data_decomposition, coeff, seuil)
print("Total recomposition - remove small coeff : ", data_recomposition)
print("---------------------------------------------------------")
print("Error calcul with absolute value :", Error1(data, seuil))
print("Error calcul with square root : ", Error2(data, seuil))
histo(coeff, seuil)
