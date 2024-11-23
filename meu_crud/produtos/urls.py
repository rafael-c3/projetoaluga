# produtos/urls.py
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    # Página para listar os produtos (disponível para todos)
    path('', views.listar_produtos, name='listar_produtos'),
    
    # URLs para adicionar, editar e remover produtos (disponíveis apenas para administradores)
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
]
