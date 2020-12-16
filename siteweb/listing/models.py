from django.db import models

# Create your models here.
class Episode(models.Model):
    CATEGORIES = [
        ('espace', 'Espace - Astronomie'),
        ('geol', 'Géologie'),
    ]
    numero = models.PositiveSmallIntegerField(primary_key=True, help_text='Numéro absolu de l\'épisode.') #à enlever je pense
    saison = models.PositiveSmallIntegerField(help_text='Numéro de la saison.') #à enlever je pense
    date = models.DateField(help_text='Date de première diffusion.')
    categorie = models.CharField(choices=CATEGORIES, max_length=10, help_text='Catégorie de l\'épisode. Si manquante, ouvrir une issue sur github.')
    titre = models.CharField(max_length=50, help_text='Titre de l\'épisode.')
    realisateur = models.CharField(max_length=50, help_text='Réalisateur de l\'épisode.')
    animateurs = models.CharField(max_length=50, help_text='Animateurs de l\'épisode.')
    resume = models.TextField(max_length=500, help_text='Résumé de l\'épisode.')
    url = models.URLField(help_text='Lien vers la vidéo en ligne de l\'épisode, sur Youtube ou autre.')