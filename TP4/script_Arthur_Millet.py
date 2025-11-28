from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import random

def uneDecompositionChaikin(data):
    data_np = np.array(data)
    new_data = []
    coeff = []
    for i in range(0,len(data),2):
        new_data.append(0.25*(-data_np[i-2] + 3*data_np[i-1] + 3*data_np[i] - data_np[i+1]))
        coeff.append(0.25*(data_np[i-2] - 3*data_np[i-1] + 3*data_np[i] - data_np[i+1]))
    return np.array(new_data), np.array(coeff)

def uneRecompositionChaikin(data, coeff):
    data_np = np.array(data)
    coeff_np = np.array(coeff)
    new_data = []
    for i in range(0,len(data)):
        new_data.append(0.75*(data_np[i] + coeff_np[i]) + 0.25*(data_np[(i+1)%len(data)] - coeff_np[(i+1)%len(data)]))
        new_data.append(0.25*(data_np[i] + coeff_np[i]) + 0.75*(data_np[(i+1)%len(data)] - coeff_np[(i+1)%len(data)]))
    return np.array(new_data)
    
def DecompositionChaikin(data):
    new_data = data
    coeff = []
    while len(new_data) > 1:
        new_data,new_coeff = uneDecompositionChaikin(new_data)
        coeff.insert(0, new_coeff)
    return np.array(new_data), coeff
    
def RecompositionChaikin(data, coeff):
    new_data = data
    for current_coeff in coeff:
        new_data = uneRecompositionChaikin(new_data, current_coeff)
    return np.array(new_data)
    
def Compression(coeff, seuil):
    new_coeff = []
    for c in coeff:
        removeSmall = np.abs(c) <= seuil
        new_coeff.append(np.where(removeSmall, 0.0, c))
    return new_coeff

def RecompositionChaikinSansPetitsCoeff(data, coeff, seuil):
    new_coeff = Compression(coeff, seuil)
    return RecompositionChaikin(data, new_coeff)

def Error1(data, seuil):
    decomposition,coeff = DecompositionChaikin(data)
    new_data = RecompositionChaikinSansPetitsCoeff(decomposition, coeff, seuil)
    return np.mean(np.abs(data - new_data))
    
def Error2(data, seuil):
    decomposition,coeff = DecompositionChaikin(data)
    new_data = RecompositionChaikinSansPetitsCoeff(decomposition, coeff, seuil)
    return np.sqrt(np.mean((data - new_data) ** 2))
    
def graphError(data):
    new_data,coeff = DecompositionChaikin(data)
    all_coeff = np.vstack(coeff)
    seuil_max = np.max(np.abs(all_coeff))
    step = seuil_max/100
    res1 = []
    res2 = []
    for i in np.arange(0,seuil_max,step):
    	res1.append([i,Error1(data,i)])
    	res2.append([i,Error2(data,i)])
    x = [pair[0] for pair in res1]
    y1 = [pair[1] for pair in res1]
    y2 = [pair[1] for pair in res2]
    plt.figure(figsize=(6,4))
    plt.plot(x, y1, marker='o', linestyle='-', color='blue', label='valeur absolue')
    plt.plot(x, y2, marker='o', linestyle='-', color='red', label='racine carré')
    plt.title("Erreur en fonction du seuil de mise à zéro des coefficients de détails")
    plt.xlabel("seuil")
    plt.ylabel("erreur")
    plt.legend()
    

def MoveSmallCoeff(coeff, seuil, move):
    new_coeff = []
    for c in coeff:
        rand = np.random.uniform(-move, move, size=c.shape)
        new_coeff.append(np.where(np.abs(c) > seuil, c, c + rand))
    return new_coeff

def test(filename, seuil, move):
	b = np.loadtxt(filename)

	b_decompose,coeff = DecompositionChaikin(b)
	b_recompose = RecompositionChaikin(b_decompose, coeff)
	b_recompose_withoutSmallCoeff = RecompositionChaikinSansPetitsCoeff(b_decompose, coeff, seuil)
	new_coeff = MoveSmallCoeff(coeff, seuil, move)
	b_recompose_moveSmallCoeff = RecompositionChaikin(b_decompose, new_coeff)

	fig1, (ax, ax1) = plt.subplots(1, 2, figsize=(12, 6))
	ax.add_patch(Polygon(b[0:len(b), :], fill=False, closed=True))
	ax.set_title("Polygone original")
	ax.set_xlim(-1, 14)
	ax.set_ylim(-1, 12)

	ax1.add_patch(Polygon(b_recompose[0:len(b_recompose), :], fill=False, closed=True))
	ax1.set_title("Polygone reconstruit après décomposition")
	ax1.set_xlim(-1, 14)
	ax1.set_ylim(-1, 12)

	fig2, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))
	ax.add_patch(Polygon(b[0:len(b), :], fill=False, closed=True))
	ax.set_title("Polygone original")
	ax.set_xlim(-1, 14)
	ax.set_ylim(-1, 12)

	ax2.add_patch(Polygon(b_recompose_withoutSmallCoeff[0:len(b_recompose_withoutSmallCoeff), :], fill=False, closed=True))
	ax2.set_title("Polygone reconstruit après mise à zéro des petits coefficiens")
	ax2.set_xlim(-1, 14)
	ax2.set_ylim(-1, 12)

	fig3, (ax, ax3) = plt.subplots(1, 2, figsize=(12, 6))
	ax.add_patch(Polygon(b[0:len(b), :], fill=False, closed=True))
	ax.set_title("Polygone original")
	ax.set_xlim(-1, 14)
	ax.set_ylim(-1, 12)

	ax3.add_patch(Polygon(b_recompose_moveSmallCoeff[0:len(b_recompose_moveSmallCoeff), :], fill=False, closed=True))
	ax3.set_title("Polygone reconstruit après déplacements de sommets")
	ax3.set_xlim(-1, 14)
	ax3.set_ylim(-1, 12)

	graphError(b)
	plt.show()

filenames = ["sh512.d", "crocodile512.d", "herisson512.d"]
seuil = float(input("Valeur du seuil : "))
move = float(input("Valeur déplacement sommets : "))
for filename in filenames:
	test(filename, seuil, move)
