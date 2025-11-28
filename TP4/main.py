import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random


random.seed(42)

CROCODILE = "crocodile512.d"
HEDGEHOG = "herisson512.d"
SEAHORSE = "sh512.d"


def decomposition_chaikin(points):
    """
    Décompose un ensemble de points en moyennes et détails selon Chaikin.
    
    Formules:
    x_i^n = 1/4 * (-x_{2i-2}^{n+1} + 3*x_{2i-1}^{n+1} + 3*x_{2i}^{n+1} - x_{2i+1}^{n+1})
    y_i^n = 1/4 * (x_{2i-2}^{n+1} - 3*x_{2i-1}^{n+1} + 3*x_{2i}^{n+1} - x_{2i+1}^{n+1})
    
    Returns: (moyennes, details) où moyennes sont les points décomposés et details les détails associés après une étape de décomposition
    """
    n = len(points)
    n_moy = n // 2
    
    moyennes = np.zeros((n_moy, 2))
    details = np.zeros((n_moy, 2))
    
    for i in range(n_moy):
        # Indices avec gestion circulaire
        i1 = (2*i - 2) % n
        i2 = (2*i - 1) % n
        i3 = (2*i) % n
        i4 = (2*i + 1) % n
        
        # Calcul des moyennes (composante X et Y)
        moyennes[i] = 0.25 * (-points[i1] + 3*points[i2] + 3*points[i3] - points[i4])
        
        # Calcul des détails
        details[i] = 0.25 * (points[i1] - 3*points[i2] + 3*points[i3] - points[i4])
    
    return moyennes, details



def recomposition_chaikin(moyennes, details):
    """
    Recompose un ensemble de points à partir des moyennes et détails selon Chaikin.
    
    Formules:
    x_{2i}^{n+1} = x_i^n - y_i^n
    x_{2i+1}^{n+1} = x_i^n + y_i^n
    
    Returns: points reconstitués après une étape de recomposition
    """
    if len(moyennes) != len(details):
        raise ValueError("Les tailles des moyennes et des détails doivent être identiques.")
    
    n_moy = len(moyennes)
    n = n_moy * 2
    
    points = np.zeros((n, 2))
    
    for i in range(n_moy):
        i_next = (i + 1) % n_moy
        points[2*i] = 0.25 * ((3*(moyennes[i] + details[i])) + (moyennes[i_next] - details[i_next]))
        points[2*i + 1] = 0.25 * ((moyennes[i] + details[i]) + 3*(moyennes[i_next] - details[i_next]))
    
    return points


def decomposition_totale(points):
    """
    Effectue une décomposition complète en moyennes et détails jusqu'à la plus petite résolution.
    
    Returns: (moyenne, détails) où moyenne est un point et détails est une liste de tableaux de détails à chaque niveau.
    """
    moyenne = points[:]
    details = []
    while len(moyenne) > 2:
        moy, det = decomposition_chaikin(moyenne)
        details.append(det)
        moyenne = moy
    return moyenne, details
        


def recomposition_totale(moyenne, details):
    """
    Recompose les points à partir de la décomposition complète en moyennes et détails.
    
    Returns: points reconstitués
    """
    n = len(moyenne)
    if n != 2:
        raise ValueError("La moyenne doit être de taille 2 pour la recomposition totale.")
    current_points = moyenne
    for det in reversed(details):
        current_points = recomposition_chaikin(current_points, det)
    return current_points

def compression_et_recomposition(moyenne, details, epsilon):
    """
    Realise une reconstitution compressée en mettant à zéro les détails de norme inférieure à epsilon.
    
    Returns: points reconstitués après compression
    """
    for detail in details:
        for elem in detail:
            if np.linalg.norm(elem) < epsilon:
                elem[:] = 0.0
    return recomposition_totale(moyenne, details)

def compression_modification_basse_resolution(moyenne, details, epsilon):
    """
    Modifie la basse résolution en modifiant légèrement les détails de norme inférieure à epsilon.
    
    Returns: points reconstitués après modification de la basse résolution
    """
    for detail in details:
        for elem in detail:
            if np.linalg.norm(elem) < epsilon:
                if random.randint(1,10) <= 5:
                    elem += epsilon
                else:
                    elem -= epsilon
    return recomposition_totale(moyenne, details)

def erreur_compression(original):
    """
    Calcule les erreurs (quadratique et absolue) entre la courbe reconstruite et la courbe compressée.
    
    Returns: erreur quadratique moyenne et erreur absolue moyenne
    """
    mse_list = []
    mae_list = []
    for eps in [0.01, 0.1, 0.5, 1.0, 2.0, 4.0, 6.0]:
        moyenne, details = decomposition_totale(original)
        recomposed = recomposition_totale(moyenne, details)
        compressed = compression_et_recomposition(moyenne, details, eps)
        recomposed = np.array(recomposed)  # Convert to numpy array for vectorized operations
        compressed = np.array(compressed)
        mse = np.mean(np.linalg.norm(recomposed - compressed, axis=1) ** 2)
        mae = np.mean(np.linalg.norm(recomposed - compressed, axis=1))
        #print(f"Epsilon: {eps}, MSE: {mse}, MAE: {mae}")
        mse_list.append(mse)
        mae_list.append(mae)
    return mse_list, mae_list

def test_decomposition_recomposition():
        for filename in [SEAHORSE, CROCODILE, HEDGEHOG]:
            file = open(filename,"r")
            lines = file.readlines()
            file.close()
            b = np.zeros((512,2))
            for i in range(512):
                ligne = lines[i].strip().split()
                b[i,0] = float(ligne[0])
                b[i,1] = float(ligne[1])
            
            decomposed,details = decomposition_totale(b)
            recomposed = recomposition_totale(decomposed,details)
            fig = plt.figure(figsize=(15,8))
            ax = fig.add_subplot(1,2,1)
            ax.add_patch(Polygon(b, fill=False, closed=True))
            ax.set_title("Original")
            plt.axis([0,13,0,11])
            ax2 = fig.add_subplot(1,2,2)
            ax2.add_patch(Polygon(recomposed, fill=False, closed=True))
            ax2.set_title("Recomposé")
            plt.suptitle("Test de décomposition/recomposition pour "+filename)
            plt.axis([0,13,0,11])
            plt.show()
            
def test_compression():
    for filename in [SEAHORSE, CROCODILE, HEDGEHOG]:
        file = open(filename,"r")
        lines = file.readlines()
        file.close()
        b = np.zeros((512,2))
        for i in range(512):
            ligne = lines[i].strip().split()
            b[i,0] = float(ligne[0])
            b[i,1] = float(ligne[1])
        
        decomposed,details = decomposition_totale(b)
        for eps in [0.01, 0.1, 0.5, 1.0, 2.0, 4.0]:
            compressed = compression_et_recomposition(decomposed, details, eps)
            fig = plt.figure(figsize=(15,8))
            ax = fig.add_subplot(1,2,1)
            ax.add_patch(Polygon(b, fill=False, closed=True))
            ax.set_title("Original")
            plt.axis([0,13,0,11])
            ax2 = fig.add_subplot(1,2,2)
            ax2.add_patch(Polygon(compressed, fill=False, closed=True))
            ax2.set_title(f"Compressé ε={eps}")
            plt.suptitle("Test de compression pour "+filename)
            plt.axis([0,13,0,11])
            plt.show()
            
def test_erreur_compression():
    for filename in [SEAHORSE, CROCODILE, HEDGEHOG]:
        file = open(filename,"r")
        lines = file.readlines()
        file.close()
        b = np.zeros((512,2))
        for i in range(512):
            ligne = lines[i].strip().split()
            b[i,0] = float(ligne[0])
            b[i,1] = float(ligne[1])
        print(f"Erreur de compression pour le fichier {filename} :")
        mse_list, mae_list = erreur_compression(b)
        plt.figure(figsize=(10,5))
        plt.plot([0.01, 0.1, 0.5, 1.0, 2.0, 4.0, 6.0], mse_list, marker='o', label='MSE')
        plt.plot([0.01, 0.1, 0.5, 1.0, 2.0, 4.0, 6.0], mae_list, marker='o', label='MAE')
        plt.xlabel('Epsilon')
        plt.ylabel('Erreur')
        plt.title(f'Erreur de compression pour {filename}')
        plt.legend()
        plt.grid(True)
        plt.show()
        
def test_modification_basse_resolution():
    for filename in [SEAHORSE, CROCODILE, HEDGEHOG]:
        file = open(filename,"r")
        lines = file.readlines()
        file.close()
        b = np.zeros((512,2))
        for i in range(512):
            ligne = lines[i].strip().split()
            b[i,0] = float(ligne[0])
            b[i,1] = float(ligne[1])
        
        decomposed,details = decomposition_totale(b)
        for eps in [0.01, 0.1, 0.5, 1.0]:
            compressed = compression_modification_basse_resolution(decomposed, details, eps)
            fig = plt.figure(figsize=(15,8))
            ax = fig.add_subplot(1,2,1)
            ax.add_patch(Polygon(b, fill=False, closed=True))
            ax.set_title("Original")
            plt.axis([0,13,0,11])
            ax2 = fig.add_subplot(1,2,2)
            ax2.add_patch(Polygon(compressed, fill=False, closed=True))
            ax2.set_title(f"modifié ε={eps}")
            plt.suptitle("Test modification basse résolution pour "+filename)
            plt.axis([0,13,0,11])
            plt.show()
        


if __name__ == "__main__":
    test_decomposition_recomposition()
    test_compression()
    test_erreur_compression()
    test_modification_basse_resolution()
    
        
    
    