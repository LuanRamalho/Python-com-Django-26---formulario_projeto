from django.urls import path
from .views import enviar_formulario, sucesso

urlpatterns = [
    path('', enviar_formulario, name='enviar_formulario'),
    path('sucesso/', sucesso, name='sucesso'),
]
