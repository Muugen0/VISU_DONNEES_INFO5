import matplotlib.pyplot as plt
import numpy as np

def decomposition_etape(signal):
    """
    1) Une étape de décomposition ondelette de Haar.
    Le signal doit être de taille paire.
    Retourne le tableau avec moyennes en première moitié, différences en seconde moitié.
    """
    if (len(signal)%2) !=0:
        raise ValueError("Le signal doit être de taille paire.")
    avg = []
    diff = []
    for i in range(len(signal)//2):
        a = (signal[2*i] + signal[2*i+1]) / 2
        d = (signal[2*i] - signal[2*i+1]) / 2
        avg.append(a)
        diff.append(d)
        
    return (avg,diff)

def decomposition_etape2(signal):
    a,b = decomposition_etape(signal)
    return a + b

#if __name__ == "__main__":
   # print(decomposition_etape2([9,7,3,5]))

def reconstruction_etape(coeffs):
    """
    2) Une étape de reconstruction ondelette de Haar.
    """
    if (len(coeffs)%2) !=0:
        raise ValueError("Le tableau des coefficients doit être de taille paire.")
    
    n = len(coeffs)//2
    approximation = coeffs[:n]
    details = coeffs[n:]
    signal = []
    for i in range(n): 
        s1 = (approximation[i] + details[i])/1
        s2 = (approximation[i] - details[i])/1
        signal.append(s1)
        signal.append(s2)
    return signal

#if __name__ == "__main__":
    #print(reconstruction_etape([8,4,1,-1]))
    #print(reconstruction_etape([6,2]))
    

def decomposition_totale(signal):
    """
    3) Décomposition totale jusqu'à taille 1.
    Le signal doit être de taille 2^n.
    """
    if (len(signal)%2) !=0:
        raise ValueError("Le signal doit être de taille 2^n.")
    approximation = signal[:]
    details = []
    while len(approximation) > 1:
        details = decomposition_etape(approximation)[1] + details
        approximation = decomposition_etape(approximation)[0]
    return approximation + details
        
#if __name__ == "__main__":
    #print(decomposition_totale([9,7,3,5]))
    

def reconstruction_totale(coeffs, original_size):
    """
    4) Reconstruction totale depuis les coefficients.
    """
    current_size = 1
    approximation = coeffs[:1]
    details = coeffs[1:]
    while current_size < original_size:
        used_details = details[:current_size]
        details = details[current_size:]
        combined_coeffs = approximation + used_details
        approximation = reconstruction_etape(combined_coeffs)
        current_size *= 2
    return approximation

#if __name__ == "__main__":
    #print(reconstruction_totale([6,2,1,-1],4))
    
def seuil(coeffs, seuil_val):
    """
    5) Mettre à zéro les coefficients de détail inférieurs au seuil.
    """
    approximation = coeffs[:1]
    details = coeffs[1:]
    new_details = []
    for d in details:
        if abs(d) < seuil_val:
            new_details.append(0)
        else:
            new_details.append(d)
    return approximation + new_details

def reconstruction_apres_seuil(coeffs, seuil_val, original_size):
    """
    5) Reconstruction après avoir mis les petits coefficients de détail à zéro.
    Utilise seuil puis reconstruction_totale.
    """
    coeffs = seuil(coeffs, seuil_val)
    return reconstruction_totale(coeffs, original_size)

def calculate_error(original, reconstructed):
    """
    6) Calcul de l’erreur entre les données d’origine et les données reconstruites approximativement.
    Utiliser norme L2.
    """
    if len(original) != len(reconstructed):
        raise ValueError("Les deux signaux doivent avoir la même taille.")
    error = 0
    for o, r in zip(original, reconstructed):
        error += (o - r) ** 2
    return error ** 0.5

def display_histogram_details(coeffs,label):
    """
    7) Histogramme des valeurs absolues des coefficients de détail.
    """

    details = coeffs[1:]
    abs_details = [abs(d) for d in details]
    plt.figure(figsize = (10,6))
    plt.hist(abs_details, bins=30)
    plt.title("Histogramme des valeurs absolues des coefficients de détail" + " : " + label)
    plt.xlabel("Valeur absolue")
    plt.ylabel("Fréquence")
    plt.grid(True)
    plt.show()
    


def display_error_vs_threshold(signal, coeffs, original_size,label):
    """
    8) Graphe de l’erreur en fonction du seuil de mise à zéro des coefficients de détail.
    """
    thresholds = np.linspace(0, max(abs(d) for d in coeffs[1:]), 50)
    errors = []
    for t in thresholds:
        reconstructed = reconstruction_apres_seuil(coeffs, t, original_size)
        error = calculate_error(signal, reconstructed)
        errors.append(error)

    plt.figure(figsize = (10,6))
    plt.plot(thresholds, errors)
    plt.title("Erreur en fonction du seuil de mise à zéro des coefficients de détail" + " : " + label)
    plt.xlabel("Seuil")
    plt.ylabel("Erreur (norme L2)")
    plt.grid(True)
    plt.show()
    

def generate_smooth_data(max_abs,size):
    """
    9) Générer des données « lisses » (par exemple sinusoïde).
    """
    import numpy as np

    x = np.linspace(0, 4 * np.pi, size)
    data = (max_abs) * np.sin(x)  # Sinusoïde entre -max_abs/2 et max_abs/2
    return data.tolist()

def generate_irregular_data(max_abs, size):
    """
    9) Générer des données « irrégulières » (par exemple bruit gaussien).
    """
    import numpy as np

    data = np.random.uniform(-max_abs, max_abs, size)
    return data.tolist()



def compare_smooth_and_irregular(max_abs,size,threshold):
    """
    10) Comparer les résultats entre des données lisses et des données irrégulières.
    """
    smooth_signal = generate_smooth_data(max_abs,size)
    irregular_signal = generate_irregular_data(max_abs,size)

    smooth_coeffs = decomposition_totale(smooth_signal)
    irregular_coeffs = decomposition_totale(irregular_signal)

    smooth_reconstructed = reconstruction_apres_seuil(smooth_coeffs, threshold, size)
    irregular_reconstructed = reconstruction_apres_seuil(irregular_coeffs, threshold, size)

    smooth_error = calculate_error(smooth_signal, smooth_reconstructed)
    irregular_error = calculate_error(irregular_signal, irregular_reconstructed)

    print(f"Erreur de reconstruction pour signal lisse: {smooth_error}")
    print(f"Erreur de reconstruction pour signal irrégulier: {irregular_error}")
    
    
    
def plot_comparison_subplots(max_abs, size, threshold):
        """
        Compare original vs reconstructed signals for smooth and irregular data.
        Displays two subplots side by side.
        """
        smooth_signal = generate_smooth_data(max_abs, size)
        irregular_signal = generate_irregular_data(max_abs, size)
        smooth_coeffs = decomposition_totale(smooth_signal)
        irregular_coeffs = decomposition_totale(irregular_signal)

        smooth_reconstructed = reconstruction_apres_seuil(smooth_coeffs, threshold, size)
        irregular_reconstructed = reconstruction_apres_seuil(irregular_coeffs, threshold, size)

        _ , axes = plt.subplots(2, 1, figsize=(12, 5))

        axes[0].plot(smooth_signal, label="Original", alpha=0.7)
        axes[0].plot(smooth_reconstructed, label="Reconstructed", alpha=0.7)
        axes[0].set_title("Smooth Signal")
        axes[0].set_xlabel("Sample")
        axes[0].set_ylabel("Value")
        axes[0].legend()
        axes[0].grid(True)

        axes[1].plot(irregular_signal, label="Original", alpha=0.7)
        axes[1].plot(irregular_reconstructed, label="Reconstructed", alpha=0.7)
        axes[1].set_title("Irregular Signal")
        axes[1].set_xlabel("Sample")
        axes[1].set_ylabel("Value")
        axes[1].legend()
        axes[1].grid(True)

        plt.tight_layout()
        plt.show()
        


if __name__ == "__main__":
    
    # Test smooth data
    smooth_signal = generate_smooth_data(40, 256)
    smooth_coeffs = decomposition_totale(smooth_signal)
    display_histogram_details(smooth_coeffs, "Smooth Signal")
    display_error_vs_threshold(smooth_signal, smooth_coeffs, 256, "Smooth Signal")
    
    # Test irregular data
    irregular_signal = generate_irregular_data(40, 256)
    irregular_coeffs = decomposition_totale(irregular_signal)
    display_histogram_details(irregular_coeffs, "Irregular Signal")
    display_error_vs_threshold(irregular_signal, irregular_coeffs, 256, "Irregular Signal")
    
    # Compare both
    compare_smooth_and_irregular(40, 256, 5)
    plot_comparison_subplots(40, 256, 5)