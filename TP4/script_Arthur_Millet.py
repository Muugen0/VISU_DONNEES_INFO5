from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

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

def uneDecompositionDouble(data):
    data_x = [elem[0] for elem in data]
    data_y = [elem[1] for elem in data]
    new_data_x, coeff_x = uneDecomposition(data_x)
    new_data_y, coeff_y = uneDecomposition(data_y)
    new_data = []
    coeff = []
    for i in range(len(new_data_x)):
        new_data.append([new_data_x[i],new_data_y[i]])
    for j in range(len(coeff_x)):
        coeff.append([coeff_x[j],coeff_y[j]])
    return new_data, coeff
    
def uneRecompositionDouble(data, coeff):
    data_x = [elem[0] for elem in data]
    data_y = [elem[1] for elem in data]
    coeff_x = [elem[0] for elem in coeff]
    coeff_y = [elem[1] for elem in coeff]
    new_data_x = uneRecomposition(data_x, coeff_x)
    new_data_y = uneRecomposition(data_y, coeff_y)
    for i in range(len(new_data_x)):
        new_data.append([new_data_x[i],new_data_y[i]])
    return new_data

def DecompositionDouble(data):
    data_x = [elem[0] for elem in data]
    data_y = [elem[1] for elem in data]
    new_data_x, coeff_x = Decomposition(data_x)
    new_data_y, coeff_y = Decomposition(data_y)
    new_data = []
    coeff = []
    for i in range(len(new_data_x)):
        new_data.append([new_data_x[i],new_data_y[i]])
    for j in range(len(coeff_x)):
        coeff.append([coeff_x[j],coeff_y[j]])
    return new_data, coeff
    
def RecompositionDouble(data, coeff):
    data_x = [elem[0] for elem in data]
    data_y = [elem[1] for elem in data]
    coeff_x = [elem[0] for elem in coeff]
    coeff_y = [elem[1] for elem in coeff]
    new_data_x = Recomposition(data_x, coeff_x)
    new_data_y = Recomposition(data_y, coeff_y)
    new_data = []
    for i in range(len(new_data_x)):
        new_data.append([new_data_x[i],new_data_y[i]])
    return new_data

def DecompositionChaikin(data):
    data_np = np.array(data)
    new_data = []
    coeff = []
    for i in range(0,len(data),2):
        new_data.append(0.25*(-data_np[i-2] + 3*data_np[i-1] + 3*data_np[i] - data_np[i+1]))
        coeff.append(0.25*(data_np[i-2] - 3*data_np[i-1] + 3*data_np[i] - data_np[i+1]))
    return np.array(new_data), np.array(coeff)

def RecompositionChaikin(data, coeff):
    data_np = np.array(data)
    coeff_np = np.array(coeff)
    new_data = []
    for i in range(0,len(data)):
        new_data.append(0.75*(data_np[i] + coeff_np[i]) + 0.25*(data_np[(i+1)%len(data)] - coeff_np[(i+1)%len(data)]))
        new_data.append(0.25*(data_np[i] + coeff_np[i]) + 0.75*(data_np[(i+1)%len(data)] - coeff_np[(i+1)%len(data)]))
    return np.array(new_data)

#filename = str(input("Nom du fichier : "))

b = np.loadtxt('sh512.d')

b_decompose,coeff = DecompositionChaikin(b)
b_recompose = RecompositionChaikin(b_decompose, coeff)

fig, (ax, ax1) = plt.subplots(1, 2, figsize=(12, 6))

ax.add_patch(Polygon(b[0:len(b), :], fill=False, closed=True))
ax.set_title("Polygone original")
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

ax1.add_patch(Polygon(b_recompose[0:len(b_recompose), :], fill=False, closed=True))
ax1.set_title("Polygone reconstruit")
ax1.set_xlim(0, 12)
ax1.set_ylim(0, 12)

plt.show()
