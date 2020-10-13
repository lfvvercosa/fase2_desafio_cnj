from django.urls import path
from . import views


urlpatterns = [
    # path('api/view_vara', view_vara)
    path('vara/<int:vara_id>/', views.view_vara),
]