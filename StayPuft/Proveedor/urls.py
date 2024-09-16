from django.urls import path
from .import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear, name='crear'),   
    path('editar/<int:id>', views.editar, name='editar'), 
    path('añadir/', views.añadir, name='añadir'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]
