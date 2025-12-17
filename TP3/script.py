import matplotlib.pyplot as plt
import random
import numpy as np

def generate_data(max_value, length):
    return [round(((random.random()*2)-1)*max_value,2) for _ in range(length)]

def generate_data_lisse(max_value, length):
    t = np.linspace(-np.pi, np.pi, length)
    raw = (
        np.sin(t)
        + 0.5*np.cos(2*t)
        + 0.3*np.sin(3*t + np.random.random()*2*np.pi)
        + 0.2*np.cos(5*t + np.random.random()*2*np.pi)
    )
    raw_min, raw_max = np.min(raw), np.max(raw)
    norm = 2*(raw - raw_min)/(raw_max - raw_min) - 1
    return [round(n,2) for n in (norm * max_value)]


def une_decomposition(data : list) :
    new_data = []
    coefs = []
    n = len(data)-1
    for i in range(0,n,2) :
        moy = (data[i] + data[i+1]) /2
        coef = data[i] - moy
        new_data.append(moy)
        coefs.append(coef)
    return new_data, coefs

def une_recomposition(data, coefs) :
    new_data = []
    for i in range(len(coefs)) :
        new_data.append(data[i] + coefs[i])
        new_data.append(data[i] - coefs[i])
    return new_data

def decomposition_totale(data) :
    new_data = data
    coefs = []
    while(len(new_data) > 1) :
        new_data, coefstmp = une_decomposition(new_data)
        coefs.extend(coefstmp)
    return new_data, coefs

def recomposition_totale(data, coefs : list) :
    new_coefs = coefs.copy()
    new_data = data
    
    while(len(new_coefs) > 1) :
        boucle_coefs = []
        for i in range(len(new_data)) :
            boucle_coefs.insert(0,new_coefs.pop(-1))
        new_data = une_recomposition(new_data, boucle_coefs)
    return new_data

def zero_coef_seuil(coefs, seuil):
    return [c if c < seuil else 0.00 for c in coefs]

def Calcul_erreur(data, new_data):
    sum = 0
    for i in range(len(data)):
        sum += abs(data[i] - new_data[i])
    return sum/len(data)
            
def Histograme_coefs(coefs, seuil) :
    coefs_abs = [abs(c) for c in coefs]
    data_range = range(int(min(coefs_abs)), int(max(coefs_abs)))
    plt.figure(figsize=(6,4))
    plt.subplot(2,1,1)
    plt.hist(coefs_abs, bins=data_range, color='skyblue', edgecolor='black')
    plt.title("Valeurs absolues des coefficients de détail")
    plt.xlabel("Coefficients de détail")
    plt.ylabel("Occurences")
    plt.axvline(x=seuil, linestyle='--', linewidth=2, color='red')
    plt.grid(True, linestyle='--', alpha=1)
    plt.show()
    
def Graphe_Erreur(data) :
    new_data, coefs = decomposition_totale(data)
    coefs_abs = [abs(c) for c in coefs]
    coef_max = max(coefs_abs)
    step = (coef_max / 100)
    x = []
    y = []
    for i in np.arange(0,coef_max,step):
        coefs_zeros = zero_coef_seuil(coefs,i)
        new_data_zeros = recomposition_totale(new_data, coefs_zeros)
        val = Calcul_erreur(new_data, new_data_zeros)
        x.append(i)
        y.append(val)
    plt.figure(figsize=(6,4))
    plt.subplot(2,1,2)
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Erreur en fonction du seuil de mise à zéro des coefficients de détails")
    plt.xlabel("seuil")
    plt.ylabel("erreur")
    plt.show()
    
def graphe_comportement(data, max, taille, seuil) :
    
    # data irregulière
    data_irreg = data
    new_data, coefs = decomposition_totale(data_irreg)
    coefs = zero_coef_seuil(coefs,seuil)
    new_data_irreg = recomposition_totale(new_data,coefs)
    
    # data lisse
    data_lisse = generate_data_lisse(max,taille)
    new_data, coefs = decomposition_totale(data_lisse)
    coefs = zero_coef_seuil(coefs,seuil)
    new_data_lisse = recomposition_totale(new_data,coefs)
    
    x = np.arange(taille)
    plt.figure(figsize=(6,8))
    plt.subplot(2,1,1)
    plt.plot(x, data_irreg, label="données originales")
    plt.plot(x, new_data_irreg, label="données reconstruites")
    plt.title("Comportement sur des données irrégulières")
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2,1,2)
    plt.plot(x,data_lisse, label="données originales")
    plt.plot(x, new_data_lisse, label="données reconstruites")
    plt.title("Comportement sur des données lisses")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    max_main = int(input("Quelle est la valeur maximale du signal ?\n"))
    length_main = int(input("Combien de valeurs voulez-vous dans le signal ?\n"))
    while (length_main % 2 != 0) :
        print("le nombre de valeur dans le signal doit être un multipde de 2")
        length_main = int(input("Combien de valeurs voulez-vous dans le signal ?\n"))
    seuil_main = int(input("A partir de quel seuil voulez-vous supprimer les ceofficients ?\n"))
    data_main = generate_data(max_main,length_main)
    # data_main = [12, 10, 7, 5, 6, 10, 4, 8]
    print(f"Données originales : {data_main}")
    
    print("=======================================================================================")
    data_1decomp, coefs_1decomp = une_decomposition(data_main)
    print(f"Données décomposés une fois : {data_1decomp}")
    print(f"Coefficents d'une décomposition : {coefs_1decomp}")
    data_1recomp = une_recomposition(data_1decomp, coefs_1decomp)
    print(f"Données resomposés une fois : {data_1recomp}")
    print(f"Comparaison arrondie à deux chiffres après la virgule :")
    print("Original\t--\tRecomposée")
    i = 0
    while (i < len(data_main) and i < len(data_1recomp)) :
        print(f"{round(data_main[i],2)}\t--\t{round(data_1recomp[i],2)}")
        i += 1
    
    print("=======================================================================================")
    data_decomp_tot, coefs_decomp_tot = decomposition_totale(data_main)
    print(f"Données totalement décomposés : {data_decomp_tot}")
    print(f"Coefficents de décomposition totale : {coefs_decomp_tot}")
    data_recomp_tot = recomposition_totale(data_decomp_tot, coefs_decomp_tot)
    print(f"Données totalement resomposée : {data_recomp_tot}")
    print(f"Comparaison arrondie à deux chiffres après la virgule :")
    print("Original\t--\tRecomposée")
    i = 0
    while (i < len(data_main) and i < len(data_recomp_tot)) :
        print(f"{round(data_main[i],2)}\t--\t{round(data_recomp_tot[i],2)}")
        i += 1
    
    print("=======================================================================================")
    coefs_decomp_tot_zeros = zero_coef_seuil(coefs_decomp_tot, seuil_main)
    data_recomp_tot_zeros = recomposition_totale(data_decomp_tot, coefs_decomp_tot_zeros)
    print(f"Données totalement resomposée avec zeros au seuil: {coefs_decomp_tot_zeros}")
    print(f"Comparaison arrondie à deux chiffres après la virgule :")
    print("Original\t--\tRecomposée")
    i = 0
    while (i < len(data_main) and i < len(coefs_decomp_tot_zeros)) :
        print(f"{round(data_main[i],2)}\t--\t{round(coefs_decomp_tot_zeros[i],2)}")
        i += 1
    
    
    print("=======================================================================================")
    erreur_recomp_tot = Calcul_erreur(data_main, data_recomp_tot)
    print(f"Erreur entre les données de départ et les données recomposées : {erreur_recomp_tot}")
    erreur_recomp_tot_zeros = Calcul_erreur(data_main, data_recomp_tot_zeros)
    print(f"Erreur entre les données de départ et les données recomposées après zéros : {erreur_recomp_tot}")
    
    Histograme_coefs(coefs_decomp_tot, seuil_main)
    Graphe_Erreur(data_main)
    graphe_comportement(data_main, max_main, length_main, seuil_main)
