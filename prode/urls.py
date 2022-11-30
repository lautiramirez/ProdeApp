from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page),
    path('partidos/', views.ver_partidos),
    path('tabla/', views.ver_tabla),
    path('historial/', views.ver_historial),
    path('amigos/', views.ver_amigos),
    path('reglas/', views.ver_reglas),

]
