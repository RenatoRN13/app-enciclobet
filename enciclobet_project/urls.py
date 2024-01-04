
from django.urls import path
from enciclobet_app import views

urlpatterns = [
    # rota, view, nome referencia
    path('', views.home, name='home'),

    path('equipe', views.equipe, name='equipe'),

    path('frequenciaMovimento', views.frequenciaMovimento, name='frequenciaMovimento')


]
