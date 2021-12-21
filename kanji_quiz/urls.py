from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:kanji>', views.portuguese_values, name='portuguese_values')
]