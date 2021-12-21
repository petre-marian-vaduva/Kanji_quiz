from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

kanji_dict = {
    '人': 'pessoa',
    '十': 'dez',
    '二': 'dois',
    '九': 'nove',
    '入': 'entrar ou inserir',
    '八': 'oito',
    '大': 'grande',
    '上': 'acima',
    '子': 'criança'
}

def index(request):
    return HttpResponse('hello world')


def get_kanji(request, kanji):
    return HttpResponse('hello world')