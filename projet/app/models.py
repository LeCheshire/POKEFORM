# membres/models.py

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# class Membre(models.Model):
#     nom = models.CharField(max_length=40)
#     age = models.IntegerField()
#     genre = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'membres'  # Nom de la table complet

class Pokemon(models.Model):
    name = models.CharField(max_length=60)
    lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    type = models.CharField(max_length=30)