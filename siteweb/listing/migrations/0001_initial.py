# Generated by Django 3.1.4 on 2020-12-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('numero', models.PositiveSmallIntegerField(help_text="Numéro absolu de l'épisode.", primary_key=True, serialize=False)),
                ('saison', models.PositiveSmallIntegerField(help_text='Numéro de la saison.')),
                ('date', models.DateField(help_text='Date de première diffusion.')),
                ('categorie', models.CharField(choices=[('espace', 'Espace - Astronomie'), ('geol', 'Géologie')], help_text="Catégorie de l'épisode. Si manquante, ouvrir une issue sur github.", max_length=10)),
                ('titre', models.CharField(help_text="Titre de l'épisode.", max_length=50)),
                ('realisateur', models.CharField(help_text="Réalisateur de l'épisode.", max_length=50)),
                ('animateurs', models.CharField(help_text="Animateurs de l'épisode.", max_length=50)),
                ('resume', models.TextField(help_text="Résumé de l'épisode.", max_length=500)),
                ('url', models.URLField(help_text="Lien vers la vidéo en ligne de l'épisode, sur Youtube ou autre.")),
            ],
        ),
    ]
