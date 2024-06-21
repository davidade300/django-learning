"""arquivo com o caminho das urls"""
from django.urls import path
from . import views


app_name = "recipes"
urlpatterns = [
    path('', views.home, name="home"),  # Home
    # no DJango <variavel> captura o valor de forma dinamica e passa para view
    # lembrar de incluir a barra final
    path("recipes/<id>/", views.recipe, name="recipe"),

]
