"""arquivo com funcao das views"""
from django.shortcuts import render
from .utils.recipes.factory import make_recipe
# from django.http import HttpResponse
# Create your views here.


def home(request):
    """
    uma funcao de view deve receber um parametro request
    """
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    """
    funcao de view para recipe
    """
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        "is_detail_page": True,
    })
