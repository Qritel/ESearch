from django.db import models
import csv
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Annonces(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Type = models.CharField(max_length=100)
    Date = models.DateField(null=True)
    Detail = models.TextField()
    URL = models.TextField()


class Concours_Services_de_lEtat(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Administration_organisatrice = models.CharField(max_length=100)
    Grade = models.CharField(max_length=200)
    Nombre_postes = models.IntegerField()
    Delai_depot = models.DateField(null=True, blank=True)
    Date_concours = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    CCPEE = models.TextField()
    CCPEO = models.TextField()
    Resultats = models.TextField()
    Desistement = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Concours_Etablissements_Entreprises_publics(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Etablissement_organisateur = models.CharField(max_length=100)
    Grade = models.CharField(max_length=200)
    Nombre_postes = models.IntegerField()
    Delai_depot = models.DateField(null=True, blank=True)
    Date_concours = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    CCPEE = models.TextField()
    CCPEO = models.TextField()
    Resultats = models.TextField()
    Desistement = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Concours_Collectivites_territoriales(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Collectivites_organisatrice = models.CharField(max_length=100)
    Grade = models.CharField(max_length=200)
    Nombre_postes = models.IntegerField()
    Delai_depot = models.DateField(null=True, blank=True)
    Date_concours = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    CCPEE = models.TextField()
    CCPEO = models.TextField()
    Resultats = models.TextField()
    Desistement = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Emplois_superieurs(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Emploi = models.CharField(max_length=100)
    Autorite_Gouvernementale = models.TextField()
    Arrete = models.TextField()
    Date_limite = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Postes_Services_de_lEtat(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Administration_organisatrice = models.TextField()
    Nombre_postes_CD = models.IntegerField()
    Nombre_postes_CS = models.IntegerField()
    Date_de_depot = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    Candidats_convoques = models.TextField()
    Resultats = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Postes_Etablissements_Entreprises_publics(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Etablissement_organisateur = models.TextField()
    Poste = models.TextField()
    Nombre_postes = models.IntegerField()
    Date_de_depot = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    Candidats_convoques = models.TextField()
    Resultats = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)


class Postes_Provinces_et_prefectures(models.Model):
    Id = models.CharField(max_length=30, primary_key=True)
    Administration_organisatrice = models.TextField()
    Nombre_postes_CD = models.IntegerField()
    Nombre_postes_CS = models.IntegerField()
    Date_de_depot = models.DateField(null=True, blank=True)
    Date_publication = models.DateField(null=True, blank=True)
    Candidats_convoques = models.TextField()
    Resultats = models.TextField()
    PPI = models.TextField(null=True)
    FA = models.TextField(null=True)
