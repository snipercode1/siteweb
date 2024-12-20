"""
URL configuration for TIMA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard
from login.views import login
# Outils proprieter
from proprieter.views import proprieter
from equipements.views import equipements
# Outils Interventions
from statistic.views import statistic
from listeIntervention.views import listeIntervention
from creerIntervention.views import creer_intervention
# Outils stocks
from stocksEquipements.views import stocks_equipements
from gestionEquipements.views import gestion_equipements
# Outils maps
from maps.views import maps
# Outils gestion de l'energie
from Electricite.views import electricite
from generator.views import generator
# Outils Documentations
from interne.views import interne
from externe.views import externe
from modeOperatoire.views import modeOperatoire


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('proprieter/', proprieter, name='proprieter'),
    path('equipements/', equipements, name='equipements'),
    path('statistic/', statistic, name='statistic'),
    path('listeIntervention/', listeIntervention, name='listeIntervention'),
    path('newIntervention/', creer_intervention, name='creer_intervention'),
    path('stocks_equipements/', stocks_equipements, name='stocks_equipements'),
    path('gestion_equipements/', gestion_equipements, name='gestion_equipements'),
    path('maps/', maps, name='maps'),
    path('electricite/', electricite, name='electricite'),
    path('generator/', generator, name='generator'),
    path('interne/', interne, name='interne'),
    path('externe/', externe, name='externe'),
    path('modeOperatoire', modeOperatoire, name='modeOperatoire'),
    
]
