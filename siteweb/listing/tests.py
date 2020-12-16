from django.test import TestCase

# Create your tests here.

###
##### Test du parsing
###

from models import Episode
import csv

filepath = '../../data/list_CPS.csv'

# Démonstration avec une liste à l'ancienne :
L = []
with open(filepath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    k = 0
    for row in csv_reader:
        numero = k #Clé = place dans le fichier .csv pour l'instant
        saison = 0 #Il n'y a pas de numéro de saison officiel
        date = row['Date']
        categorie = row['Catégorie']
        titre = row['Titre']
        realisateur = row['Réalisateur']
        animateurs = row['Animateurs']
        resume = row['Résumé']
        url = row['Lien Youtube']
        L.append([numero, saison, date, titre, realisateur, animateurs, resume, url])
        k += 1
print(L[21])


# Test de remplissage de la BDD :
with open(filepath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    k = 0
    for row in csv_reader:
        episode = EpisodePerson(numero = k, #Clé = place dans le fichier .csv pour l'instant
                               saison = 0, #Il n'y a pas de numéro de saison officiel
                                date = row['Date'],
                                categorie = row['Catégorie'],
                                titre = row['Titre'],
                                realisateur = row['Réalisateur'],
                                animateurs = row['Animateurs'],
                                resume = row['Résumé'],
                                url = row['Lien Youtube'])
        episode.save()
        k += 1

print(Episode.objects.values_list('titre', flat=True))
