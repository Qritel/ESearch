"""ESearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myapp.views import *

handler404 = 'myapp.views.handler404'
handler500 = 'myapp.views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^concours_services_etat/', concours1, name='concours1'),
    url(r'^concours_etablissements_entreprises_publics/', concours2, name='concours2'),
    url(r'^concours_collectivités_territoriales/', concours3, name='concours3'),
    url(r'^emplois_supérieurs/', emplois_sup, name='emplois_sup'),
    url(r'^postes_services_etat/', postes1, name='postes1'),
    url(r'^postes_Provinces_préfectures/', postes2, name='postes2'),
    url(r'^postes_etablissements_entreprises_publics/', postes3, name='postes3'),
    url(r'^contact/', contact, name='contact'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^management/logout/$', auth_views.logout, name='logout'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]
