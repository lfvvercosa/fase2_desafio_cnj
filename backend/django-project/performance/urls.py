from django.urls import path
from . import views


urlpatterns = [
    # Home
    path('', views.home),

    # Varas
    path('api/v1/varas/', views.varas_list),
    path('api/v1/varas/<int:vara_id>/', views.vara_details),
    path('api/v1/varas/bestVarasOnStep/', views.best_varas_on_step),

    # Etapas
    path('api/v1/steps/bestSteps/', views.best_steps),
    path('api/v1/steps/worstSteps/', views.worst_steps),

    # Processos
    path('api/v1/processes/bestVaras/', views.best_varas),

    # Comentarios
    path('api/v1/comments/', views.comments_list),
    path('api/v1/comments/<int:comment_id>/', views.comment),
]
