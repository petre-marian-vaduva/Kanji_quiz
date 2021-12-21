from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:kanji>', views.portuguese_values_by_number),
    path('<str:kanji>', views.portuguese_values, name='portuguese_values')
]