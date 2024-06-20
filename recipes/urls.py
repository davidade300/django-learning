"""arquivo com o caminho das urls"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),  # Home
    # no DJango <variavel> captura o valor de forma dinamica e passa para view
    # lembrar de incluir a barra final
    path("recipes/<id>/", views.recipe),

]
