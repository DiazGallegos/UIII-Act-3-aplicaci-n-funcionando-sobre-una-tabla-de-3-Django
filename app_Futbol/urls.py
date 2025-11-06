from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_futbol, name='inicio_futbol'),
    path('equipos/agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('equipos/', views.ver_equipos, name='ver_equipos'),
    path('equipos/actualizar/<int:id>/', views.actualizar_equipo, name='actualizar_equipo'),
    path('equipos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_equipo, name='realizar_actualizacion_equipo'),
    path('equipos/borrar/<int:id>/', views.borrar_equipo, name='borrar_equipo'),
    path('equipos/realizar_borrado/<int:id>/', views.realizar_borrado_equipo, name='realizar_borrado_equipo'),
]