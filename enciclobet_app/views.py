from django.shortcuts import render
# from enciclobet_app.utils import popula_base
from enciclobet_app.utils.operacional import Operacional
from enciclobet_app.utils import CONSTANTES
from .models import Infos

# Create your views here.

def home(request):
    listaTimes = {
        'listaTimes': CONSTANTES.times
    }

    return render(request, 'paginas/home.html', listaTimes)

def frequenciaMovimento(request):
    constantes = {
        'listaTimes': CONSTANTES.times,
        'listaTemporadas': CONSTANTES.temporadas
    }

    return render(request, 'paginas/frequencia-movimento.html', constantes)

def equipe(request):
    casa = request.POST.get('casa')
    visitante = request.POST.get('visitante')

    filtros = { 
                'odd1': 0, 
                'odd2': 0, 
                'home': casa, 
                'away': visitante, 
                'league': '', 
                'season': '2023'
            }

    # infoDaBase = Operacional.infoBackFavorito1T(filtros)

    infoParaHTML = Infos()

    # infoParaHTML.resultCasa = infoDaBase['resultCasa']
    # infoParaHTML.resultVisitante = infoDaBase['resultVisitante']

    infos = {
        'infos': Operacional.infoBackFavorito1T(filtros)
    }

    return render(request, 'paginas/info-equipes.html', infos)
