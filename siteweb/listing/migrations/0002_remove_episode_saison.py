# Generated by Django 3.1.4 on 2020-12-17 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='saison',
        ),
    ]
