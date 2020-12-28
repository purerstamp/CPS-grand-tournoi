from elo import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli

# Create your tests here.

###
##### Simulation du classement elo
###

# Initialisation
Nelem = 100
L = []

N = 1000 #Nombre de confrontations

show = 'histogramme'
showElo = False

for k in range(Nelem):
    L.append([0,1500])    

# Fonction d'affichage
def show_values(L, title, sort=False, showElo=True):
    T = []
    for k in range(Nelem):
        if showElo:
            T.append(L[k][1])
            plt.ylabel('Elo')
        else:
            T.append(L[k][0])
            plt.ylabel('Nombre de confrontations')
    if sort:
        T.sort()
    plt.scatter([k for k in range(Nelem)], T) 
    plt.xlabel('Épisode')
    plt.title(title)
    plt.show()

def show_histogramme(L, title, sort=False, showElo=False):
    T = []
    for k in range(Nelem):
        if showElo:
            T.append(L[k][1])
        else:
            T.append(L[k][0])            
    if showElo:
        plt.hist(T, range=(1200,1800), bins=25, density=True, edgecolor='black')
        plt.xlabel('Elo')
    else:
        plt.hist(T, bins=25, density=True, color='g', edgecolor='black')
        plt.xlabel('Nombre de confrontations')
    plt.ylabel('Fréquence')
    plt.title(title)
    plt.show()


# Simulation de l'évolution du classement après N confrontations :

if (show=='values'):
    show_values(L, 'k = 0', sort=False, showElo=showElo)
elif (show=='histogramme'):
    show_histogramme(L, 'k = 0', showElo=showElo)
    
for k in range(N):
    A = np.random.randint(0,Nelem)
    B = np.random.randint(0,Nelem)
    iter = 1 
    while((B==A) or iter>=1000):
        B = np.random.randint(0,Nelem)
        iter += 1
    #Duel entre A et B :
    p_A_vainqueur = proba_gain(L[A][1]-L[B][1])
    A_vainqueur = bernoulli.rvs(p_A_vainqueur)
    
    #Calcul des coefficients K :
    K_A = evaluation_K(L[A][0], L[A][1])
    K_B = evaluation_K(L[B][0], L[B][1])
    
    #Actualisation des scores :
    new_elo_A, new_elo_B = confrontation(A_vainqueur,
                                         L[A][1], K_A,
                                         L[B][1], K_B)
    L[A][0] += 1
    L[A][1] = new_elo_A
    L[B][0] += 1
    L[B][1] = new_elo_B
    
    if ((k+1)%50==0):
        title = 'k = '+str(k+1)
        if (show=='values'):
            show_values(L, title, sort=True, showElo=showElo)
        elif (show=='histogramme'):
            show_histogramme(L, title, showElo=showElo)

    