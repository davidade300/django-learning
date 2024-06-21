"""
neste arquivo adicionamos as classes modelo
o framework criará automaticamente as tabelas baseadas nos modelos
"""
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """
    CLASSE ASSOCIATIVA
    """
    name = models.CharField(max_length=65)


class Recipe(models.Model):
    """
    cada coluna(campo) da tabela é um atributo da classe
    """

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    Author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
