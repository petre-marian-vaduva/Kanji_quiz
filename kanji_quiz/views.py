from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

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
    kanji_keys = list(kanji_dict.keys())
    return render(request, 'kanji_quiz/index.html', {
        'kanji_keys': kanji_keys
    })

def portuguese_values(request, kanji):
    kanji_value = kanji_dict[kanji]
    return render(request, 'kanji_quiz/portuguese.html', {
        'kanji_value': kanji_value
    })

def portuguese_values_by_number(request, kanji):
    kanji_keys = list(kanji_dict.keys())
    path_redirected = reverse('portuguese_values', args=[
        kanji_keys[kanji]
    ])
    return HttpResponseRedirect(path_redirected)
