from django.contrib import admin
from .models import *

# Register your models here.


class Annonces_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Type', 'Date', 'Detail', 'URL']


class Concours1_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Administration_organisatrice', 'Grade', 'Nombre_postes', 'Delai_depot',
                    'Date_concours', 'Date_publication', 'CCPEE', 'CCPEO', 'Resultats', 'Desistement', 'PPI', 'FA']


class Concours2_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Etablissement_organisateur', 'Grade', 'Nombre_postes', 'Delai_depot',
                    'Date_concours', 'Date_publication', 'CCPEE', 'CCPEO', 'Resultats', 'Desistement', 'PPI', 'FA']


class Concours3_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Collectivites_organisatrice', 'Grade', 'Nombre_postes', 'Delai_depot',
                    'Date_concours', 'Date_publication', 'CCPEE', 'CCPEO', 'Resultats', 'Desistement', 'PPI', 'FA']


class Emplois_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Emploi', 'Autorite_Gouvernementale',
                    'Arrete', 'Date_limite', 'Date_publication', 'PPI', 'FA']


class Postes1_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Administration_organisatrice', 'Nombre_postes_CD', 'Nombre_postes_CS',
                    'Date_de_depot', 'Date_publication', 'Candidats_convoques', 'Resultats', 'PPI', 'FA']


class Postes2_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Etablissement_organisateur', 'Poste', 'Nombre_postes',
                    'Date_de_depot', 'Date_publication', 'Candidats_convoques', 'Resultats', 'PPI', 'FA']


class Postes3_Admin(admin.ModelAdmin):
    list_display = ['Id', 'Administration_organisatrice', 'Nombre_postes_CD', 'Nombre_postes_CS',
                    'Date_de_depot', 'Date_publication', 'Candidats_convoques', 'Resultats', 'PPI', 'FA']


admin.site.register(Annonces, Annonces_Admin)
admin.site.register(Concours_Services_de_lEtat, Concours1_Admin)
admin.site.register(Concours_Etablissements_Entreprises_publics, Concours2_Admin)
admin.site.register(Concours_Collectivites_territoriales, Concours3_Admin)
admin.site.register(Emplois_superieurs, Emplois_Admin)
admin.site.register(Postes_Services_de_lEtat, Postes1_Admin)
admin.site.register(Postes_Etablissements_Entreprises_publics, Postes2_Admin)
admin.site.register(Postes_Provinces_et_prefectures, Postes3_Admin)
