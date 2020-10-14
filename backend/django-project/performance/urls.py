from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.home),

    # Varas
    path('api/v1/varas/', views.lista_varas),
    path('api/v1/varas/<int:vara_id>/', views.detalhes_vara),
    path('api/v1/varas/melhoresVarasNaEtapa/', views.melhores_varas_na_etapa),

    # Etapas
    path('api/v1/etapas/melhoresEtapas/', views.melhores_etapas),
    path('api/v1/etapas/pioresEtapas/', views.piores_etapas),

    # Processos
    path('api/v1/processos/melhoresVaras/', views.melhores_varas),

    # Comentarios
    path('api/v1/comentarios/', views.lista_comentarios),
    path('api/v1/comentarios/<int:identificador>/', views.comentario),
]
