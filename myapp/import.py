import csv
import sys
import os
import datetime

sys.path.append("/home/kami/ESearch/ESearch")
sys.path.append("/home/kami/ESearch")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from myapp.models import *

# data = csv.reader(open("/home/kami/ESearch/myapp/scripts_files/annonces.csv"), delimiter=",")
# for row in data:
#     if row[0] != "Id":
#         annonces = Annonces()
#         annonces.Id = row[0]
#         annonces.Type = row[1]
#         annonces.Date = datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%Y-%d-%m")
#         annonces.Detail = row[3]
#         annonces.URL = row[4]
#         annonces.save()

# data = csv.reader(
#     open("/home/kami/ESearch/myapp/scripts_files/Concours/Services_de_l'Etat.csv"), delimiter=",")
# for row in data:
#     if row[0].strip() != "Id":
#         concours = Concours_Services_de_lEtat()
#         concours.Id = row[0]
#         concours.Administration_organisatrice = row[1]
#         concours.Grade = row[2]
#         concours.Nombre_postes = int(row[3])
#         concours.Delai_depot = row[4]
#         concours.Date_concours = row[5]
#         concours.Date_publication = row[6]
#         concours.CCPEE = row[7]
#         concours.CCPEO = row[8]
#         concours.Resultats = row[9]
#         concours.Desistement = row[10]
#         concours.PPI = row[11]
#         concours.FA = row[12]
#         concours.save()
#
# data = csv.reader(open(
#     "/home/kami/ESearch/myapp/scripts_files/Concours/Etablissements_Entreprises_publics.csv"), delimiter=",")
# for row in data:
#     if row[0].strip() != "Id":
#         concours = Concours_Etablissements_Entreprises_publics()
#         concours.Id = row[0]
#         concours.Etablissement_organisateur = row[1]
#         concours.Grade = row[2]
#         concours.Nombre_postes = int(row[3])
#         concours.Delai_depot = row[4]
#         concours.Date_concours = row[5]
#         concours.Date_publication = row[6]
#         concours.CCPEE = row[7]
#         concours.CCPEO = row[8]
#         concours.Resultats = row[9]
#         concours.Desistement = row[10]
#         concours.PPI = row[11]
#         concours.FA = row[12]
#         concours.save()
#
# data = csv.reader(open(
#     "/home/kami/ESearch/myapp/scripts_files/Concours/Collectivités_territoriales.csv"), delimiter=",")
# for row in data:
#     if row[0].strip() != "Id":
#         concours = Concours_Collectivites_territoriales()
#         concours.Id = row[0]
#         concours.Collectivites_organisatrice = row[1]
#         concours.Grade = row[2]
#         concours.Nombre_postes = int(row[3])
#         concours.Delai_depot = row[4]
#         concours.Date_concours = row[5]
#         concours.Date_publication = row[6]
#         concours.CCPEE = row[7]
#         concours.CCPEO = row[8]
#         concours.Resultats = row[9]
#         concours.Desistement = row[10]
#         concours.PPI = row[11]
#         concours.FA = row[12]
#         concours.save()

# data = csv.reader(open(
#     "/home/kami/ESearch/myapp/scripts_files/Emplois_supérieurs/Emplois.csv"), delimiter=",")
# for row in data:
#     if row[0].strip() != "Id":
#         emplois = Emplois_superieurs()
#         emplois.Id = row[0]
#         emplois.Emploi = row[1]
#         emplois.Autorite_Gouvernementale = row[2]
#         emplois.Arrete = row[3]
#         emplois.Date_limite = row[4]
#         emplois.Date_publication = row[5]
#         emplois.PPI = row[6]
#         emplois.FA = row[7]
#         emplois.save()

data = csv.reader(open(
    "/home/kami/ESearch/myapp/scripts_files/Postes_de_responsabilité/Services_de_l'Etat.csv"), delimiter=",")
for row in data:
    if row[0].strip() != "Id":
        postes = Postes_Services_de_lEtat()
        postes.Id = row[0]
        postes.Administration_organisatrice = row[1]
        postes.Nombre_postes_CD = int(row[2])
        postes.Nombre_postes_CS = int(row[3])
        postes.Date_de_depot = row[4]
        postes.Date_publication = row[5]
        postes.Candidats_convoques = row[6]
        postes.Resultats = row[7]
        postes.PPI = row[8]
        postes.FA = row[9]
        postes.save()

data = csv.reader(open(
    "/home/kami/ESearch/myapp/scripts_files/Postes_de_responsabilité/Etablissements et Entreprises publics.csv"), delimiter=",")
for row in data:
    if row[0].strip() != "Id":
        postes = Postes_Etablissements_Entreprises_publics()
        postes.Id = row[0]
        postes.Etablissement_organisateur = row[1]
        postes.Poste = row[2]
        postes.Nombre_postes = int(row[3])
        postes.Date_de_depot = row[4]
        postes.Date_publication = row[5]
        postes.Candidats_convoques = row[6]
        postes.Resultats = row[7]
        postes.PPI = row[8]
        postes.FA = row[9]
        postes.save()

data = csv.reader(open(
    "/home/kami/ESearch/myapp/scripts_files/Postes_de_responsabilité/Provinces_et_préfectures.csv"), delimiter=",")
for row in data:
    if row[0].strip() != "Id":
        postes = Postes_Provinces_et_prefectures()
        postes.Id = row[0]
        postes.Administration_organisatrice = row[1]
        postes.Nombre_postes_CD = int(row[2])
        postes.Nombre_postes_CS = int(row[3])
        postes.Date_de_depot = row[4]
        postes.Date_publication = row[5]
        postes.Candidats_convoques = row[6]
        postes.Resultats = row[7]
        postes.PPI = row[8]
        postes.FA = row[9]
        postes.save()
