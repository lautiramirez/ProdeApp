from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    data = "Main Page"
    return render(request, 'layouts/index.html', {
        'param': data
    })

def ver_partidos(request):
    data = "Partidos"
    return render(request, 'layouts/partidos.html', {
        'param': data
    })

def ver_tabla(request):
    data = "Tabla"
    return render(request, 'layouts/tabla.html', {
        'param': data
    })   

def ver_historial(request):
    data = "Historial"
    return render(request, 'layouts/historial.html', {
        'param': data
    })

def ver_amigos(request):
    data = "Amigos"
    return render(request, 'layouts/amigos.html', {
        'param': data
    })

def ver_reglas(request):
    data = "Reglas"
    return render(request, 'layouts/reglas.html', {
        'param': data
    })