from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
        path("registrarColegio/", views.registrarColegio),
        path("eliminarColegio/<codigo>", views.eliminarColegio),
        path("edicionColegio/<codigo>", views.edicionColegio),
        path("editarColegio/", views.editarColegio),

]
