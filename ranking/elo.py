#test
import numpy as np

###
##### Fonctions :
###

def proba_gain(D):
    #probabilité de gain en fonction de la différence D de points Elo 
    #entre 2 éléments.
    return(1/(1+10**(-D/400))) #400 est la constante utilisée aux échecs

def evaluation_K(N, elo):
    #Renvoie la valeur du paramètre K pour un élément ayant participé à 
    #N confrontations (selon la nome FIDE)
    if (N<=30):
        K = 40
    else:
        if (elo<=2400):
            K = 20
        else:
            K = 10
    return(K)

def confrontation(A_vainqueur, elo_A, K_A, elo_B, K_B):
    #fonction actualisant les classements Elo entre les deux éléments A et B.
    #A_vainqueur=1 <-> A a remporté la partie
    #A_vainqueur=0 <-> B a remporté la partie
    D = max(-400,elo_A-elo_B) #la différence est ramenée à +/- 400
    D = min(D,400)
    new_elo_A = max(0,elo_A + K_A*(A_vainqueur-proba_gain(elo_A-elo_B)))
    new_elo_B = max(0,elo_B + K_B*(1-A_vainqueur-proba_gain(elo_B-elo_A)))
    return(new_elo_A, new_elo_B)